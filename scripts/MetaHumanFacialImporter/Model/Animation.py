from typing import List, Dict

from maya.api import OpenMayaAnim as oma2, OpenMaya as om2

from MetaHumanFacialImporter.Model.FacialRig import FacsDrivenController

anim_curve_cache: Dict[str, oma2.MFnAnimCurve] = {}


def set_keys(fps_values: List[int], action_unit_values: Dict[str, List[float]], action_unit_ctrls: Dict[str, List[FacsDrivenController]]):
    for action_unit, values in action_unit_values.items():
        ctrls = action_unit_ctrls[action_unit]
        for ctrl in ctrls:
            add_keys(ctrl, fps_values, values)


def add_keys(ctrl: FacsDrivenController, times: List[float], values: List[float]):
    try:
        anim_curve = anim_curve_cache[ctrl.name_and_attribute]
    except KeyError:
        # キャッシュがないようならば、探すか作る
        depend_node = get_depend_node(ctrl.name)
        dependency_node = om2.MFnDependencyNode(depend_node)
        attr_plug: om2.MPlug = dependency_node.findPlug(ctrl.attribute, 0)
        anim_curve = find_anim_curve(attr_plug)
        if not anim_curve:
            anim_curve = create_anim_curve(attr_plug)
        anim_curve_cache[ctrl.name_and_attribute] = anim_curve

    anim_curve.addKeys(times, values)


def find_anim_curve(attr_plug: om2.MPlug) -> oma2.MFnAnimCurve:
    m_it_dependency_graph = om2.MItDependencyGraph(attr_plug,
                                                   om2.MItDependencyGraph.kUpstream,
                                                   om2.MItDependencyGraph.kPlugLevel)
    anim_curve = None
    while not m_it_dependency_graph.isDone():
        current_node: om2.MObject = m_it_dependency_graph.currentNode()
        if current_node.hasFn(om2.MFn.kAnimCurve):
            anim_curve = oma2.MFnAnimCurve(current_node)
        m_it_dependency_graph.next()
    return anim_curve


def create_anim_curve(attr_plug: om2.MPlug) -> oma2.MFnAnimCurve:
    dag_modifier = om2.MDGModifier()

    created_node = dag_modifier.createNode('animCurveTL')
    anim_curve = oma2.MFnAnimCurve()
    anim_curve.setObject(created_node)
    anim_curve.setName(attr_plug.name().replace('.', '_'))

    anim_curve_output_plug = anim_curve.findPlug('output', 0)

    dag_modifier.connect(anim_curve_output_plug, attr_plug)
    dag_modifier.doIt()

    return anim_curve


def get_depend_node(target: str) -> om2.MObject:
    selection: om2.MSelectionList = om2.MGlobal.getSelectionListByName(target)
    depend_node = selection.getDependNode(0)
    return depend_node
