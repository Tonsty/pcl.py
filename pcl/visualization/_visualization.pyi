from enum import Enum
from typing import Any, Tuple, List, Callable

from numpy import ndarray

from ._connection import BoostConnection
from ..PointCloud import PointCloud

class KeyboardEvent:
    def isAltPressed(self) -> bool: ...
    def isCtrlPressed(self) -> bool: ...
    def isShiftPressed(self) -> bool: ...
    @property
    def KeyCode(self) -> str: ...
    @property
    def KeySym(self) -> str: ...
    def keyDown(self) -> bool: ...
    def keyUp(self) -> bool: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...

class MouseEvent_Type(Enum):
    MouseMove: int
    MouseButtonPress: int
    MouseButtonRelease: int
    MouseScrollDown: int
    MouseScrollUp: int
    MouseDblClick: int

class MouseEvent_MouseButton(Enum):
    NoButton: int
    LeftButton: int
    MiddleButton: int
    RightButton: int
    VScroll: int

class MouseEvent:
    @property
    def Type(self) -> MouseEvent_Type: ...
    @property
    def Button(self) -> MouseEvent_MouseButton: ...
    @property
    def X(self) -> int: ...
    @property
    def Y(self) -> int: ...
    @property
    def KeyboardModifiers(self) -> int: ...
    @property
    def SelectionMode(self) -> bool: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...

class PointPickingEvent:
    @property
    def Point(self) -> Tuple[float, float, float]: ...
    @property
    def PointIndex(self) -> int: ...
    @property
    def Points(self) -> List[Tuple[float, float, float]]: ...
    @property
    def PointIndices(self) -> Tuple[int, int]: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...

class AreaPickingEvent:
    @property
    def PointIndices(self) -> List[int]: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...

class VisualizerInteractorStyle:
    @property
    def CameraFile(self) -> str: ...
    CameraFile.setter
    def CameraFile(self, value: str) -> None: ...

    def saveCameraParameters(self, file: str): ...
    def loadCameraParameters(self, file: str): ...

class RenderingProperties(Enum):
    PointSize: int
    Opacity: int
    LineWidth: int
    FontSize: int
    Color: int
    Representation: int
    ImmediateRendering: int
    Shading: int

class RenderingRepresentationProperties(Enum):
    Points: int
    WireFrame: int
    Surface: int

class ShadingRepresentationProperties(Enum):
    Flat: int
    Gouraud: int
    Phong: int

class Visualizer:
    def __init__(self, name: str = "", create_interactor: bool = True): ...

    def setFullScreen(self, mode: bool) -> None: ...
    def setWindowName(self, name: str) -> None: ...
    def setWindowBorders(self, mode: bool) -> None: ...
    def setBackgroundColor(self, r: float, g: float, b: float, viewport: int = 0) -> None: ...

    def registerKeyboardCallback(self, callback: Callable[[KeyboardEvent], Any]) -> BoostConnection: ...
    def registerMouseCallback(self, callback: Callable[[MouseEvent], Any]) -> BoostConnection: ...
    def registerPointPickingCallback(self, callback: Callable[[PointPickingEvent], Any]) -> BoostConnection: ...
    def registerAreaPickingCallback(self, callback: Callable[[AreaPickingEvent], Any]) -> BoostConnection: ...

    def spin(self) -> None: ...
    def spinOnce(self, time: int = 1, force_redraw: bool = False) -> None: ...

    def addCoordinateSystem(self, scale: float = 1, x: float = 0, y: float = 0, z: float = 0, t: ndarray = None, id: str = "reference", viewport: int = 0) -> None: ...
    def removeCoordinateSystem(self, id = "cloud", viewport: int = 0) -> None: ...

    def removePointCloud(self, id: str = "cloud", viewport: int = 0) -> None: ...
    def removePolygonMesh(self, id: str = "polygon", viewport: int = 0) -> None: ...
    def removeShape(self, id: str = "cloud", viewport: int = 0) -> None: ...
    def removeText3D(self, id: str = "cloud", viewport: int = 0) -> None: ...
    def removeAllPointClouds(self, viewport: int = 0) -> None: ...
    def removeAllShapes(self, viewport: int = 0) -> None: ...

    def addText(self, text: str, xpos: int, ypos: int, fontsize: int = 10, color: Tuple[float, float, float] = [1,1,1], id: str = "", viewport: int = 0) -> None: ...
    def updateText(self, text: str, xpos: int, ypos: int, fontsize: int = 10, color: Tuple[float, float, float] = [1,1,1], id: str = "") -> None: ...
    def addText3D(self, text: str, position, text_scale: float = 1, color: Tuple[float, float, float] = [1,1,1], id: str = "", viewport: int = 0) -> None: ...
    def addPointCloudNormals(self, cloud: PointCloud, normals: PointCloud = None, level: int = 100, scale: float = 1, id: str = "cloud", viewport: int = 0) -> None: ...
    # def addPointCloudPrincipalCurvatures(self, cloud: PointCloud, normals: PointCloud, pcs: PointCloud, level: int = 100, scale: float = 1, id: str = "cloud", viewport: int = 0) -> None: ...
    # def addPointCloudIntensityGradients(self, cloud: PointCloud, gradients: PointCloud , level: int = 100, scale: float = 1e-6, id: str = "cloud", viewport: int = 0) -> None: ...

    # def addCorrespondences(self, source_points: PointCloud, target_points: PointCloud, correspondences, id: str = "", viewport: int = 0) -> None: ...
    # def removeCorrespondences (self, id: str = "correspondences", viewport: int = 0) -> None: ...

    def updateShapePose(self, id: str, pose: ndarray) -> None: ...
    def updatePointCloudPose(self, id: str, pose: ndarray) -> None: ...

    def wasStopped(self) -> bool: ...
    def resetStoppedFlag(self) -> None: ...
    def close(self) -> None: ...
    def createViewPort(self, xmin: float, ymin: float, xmax: float, ymax: float) -> int: ...
    def createViewPortCamera(self, viewport: int) -> None: ...

    def addPointCloud(self, cloud: PointCloud, color: Tuple[float, float, float] = [1,1,1], field: str = None, color_handler: Callable[[PointCloud], ndarray] = None, static_mapping: bool = True, id: str = "", viewport: int = 0) -> None: ...
    def updatePointCloud(self, cloud: PointCloud, id: str = "") -> None: ...

    def addLine(self, p1, p2, color: Tuple[float, float, float] = [1,1,1], id: str = "", viewport: int = 0) -> None: ...
    def addArrow(self, p1, p2, line_color: Tuple[float, float, float] = [1,1,1], text_color: Tuple[float, float, float] = [1,1,1], display_length: bool = False, id: str = "", viewport: int = 0) -> None: ...
    def addSphere(self, center, radius: float, color: Tuple[float, float, float] = [1,1,1], id: str = "", viewport: int = 0) -> None: ...
    def updateSphere(self, center, radius: float, color: Tuple[float, float, float] = [1,1,1], id: str = "") -> None: ...
    def addCylinder(self, point_on_axis, axis_direction, radius: float, id: str = "", viewport: int = 0) -> None: ...
    def addPlane(self, coeffs, id: str = "", viewport: int = 0) -> None: ...
    def addCircle(self, center, radius: float, id: str = "", viewport: int = 0) -> None: ...
    def addCube(self, translation, rotation, width: float, height: float, depth: float, id: str = "", viewport: int = 0) -> None: ...

    def getColorHandlerIndex(self, id: str) -> int: ...
    def getGeometryHandlerIndex(self, id: str) -> int: ...
    def updateColorHandlerIndex(self, id: str, index: int) -> None: ...
    def setShapeRenderingProperties(self, property, value, id: str, viewport: int = 0) -> None: ...
    def setPointCloudRenderingProperties(self, property, value, id: str, viewport: int = 0) -> None: ...
    def setRepresentationToSurfaceForAllActors(self) -> None: ...
    def setRepresentationToPointsForAllActors(self) -> None: ...
    def setRepresentationToWireframeForAllActors(self) -> None: ...

    def initCameraParameters(self) -> None: ...
    def getCameraParameters(self, argv: List[str]) -> None: ...
    def cameraParamsSet(self) -> bool: ...
    def updateCamera(self) -> None: ...
    def resetCamera(self) -> None: ...
    def resetCameraViewpoint(self, id: str = "") -> None: ...
    def setCameraPosition(self, position: Tuple[float, float, float], view_up: Tuple[float, float, float], focal_point: Tuple[float, float, float] = None, viewport: int = 0) -> None: ...
    def setCameraFieldOfView(self, fovy: float, viewport: int = 0) -> None: ...
    def setCameraClipDistances(self, near: float, far: float, viewport: int = 0) -> None: ...

    def setPosition(self, x: int, y: int) -> None: ...
    def setSize(self, xw: int, yw: int) -> None: ...
    def setUseVbos(self, use_vbox: bool) -> None: ...
    def createInteractor(self) -> None: ...
    def saveScreenshot(self, file: str) -> None: ...
    def setShowFPS(self, show_fps: bool) -> None: ...

    def getInteractorStyle(self) -> VisualizerInteractorStyle: ...

    def render(self) -> None: ...
