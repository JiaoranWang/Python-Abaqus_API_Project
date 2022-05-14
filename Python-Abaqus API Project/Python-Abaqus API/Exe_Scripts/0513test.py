# -*- coding: mbcs -*-
from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *
mdb.openAcis('C:/Users/jiaor/Desktop/2022 STUDY/Parts.sat', scaleFromFile=OFF)
mdb.models['Model-1'].PartFromGeometryFile(combine=False, dimensionality=
    THREE_D, geometryFile=mdb.acis, name='Parts', type=DEFORMABLE_BODY)
mdb.models['Model-1'].Material(name='Material-1')
mdb.models['Model-1'].materials['Material-1'].Elastic(table=((500000.0, 0.4),
    ))
mdb.models['Model-1'].Material(name='Material-2')
mdb.models['Model-1'].materials['Material-2'].Elastic(table=((29500.0, 0.3), ))
mdb.models['Model-1'].HomogeneousSolidSection(material='Material-1', name=
    'Section-1', thickness=None)
mdb.models['Model-1'].HomogeneousSolidSection(material='Material-2', name=
    'Section-2', thickness=None)
mdb.models['Model-1'].parts['Parts'].Set(cells=
    mdb.models['Model-1'].parts['Parts'].cells.getSequenceFromMask(('[#8000 ]',
    ), ), name='Set-1')
mdb.models['Model-1'].parts['Parts'].SectionAssignment(offset=0.0, offsetField=
    '', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Parts'].sets['Set-1'], sectionName='Section-1'
    , thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Parts'].Set(cells=
    mdb.models['Model-1'].parts['Parts'].cells.getSequenceFromMask((
    '[#40000 ]', ), ), name='Set-2')
mdb.models['Model-1'].parts['Parts'].SectionAssignment(offset=0.0, offsetField=
    '', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Parts'].sets['Set-2'], sectionName='Section-1'
    , thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Parts'].Set(cells=
    mdb.models['Model-1'].parts['Parts'].cells.getSequenceFromMask((
    '[#20000 ]', ), ), name='Set-3')
mdb.models['Model-1'].parts['Parts'].SectionAssignment(offset=0.0, offsetField=
    '', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Parts'].sets['Set-3'], sectionName='Section-1'
    , thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Parts'].Set(cells=
    mdb.models['Model-1'].parts['Parts'].cells.getSequenceFromMask((
    '[#10000 ]', ), ), name='Set-4')
mdb.models['Model-1'].parts['Parts'].SectionAssignment(offset=0.0, offsetField=
    '', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Parts'].sets['Set-4'], sectionName='Section-1'
    , thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Parts'].Set(cells=
    mdb.models['Model-1'].parts['Parts'].cells.getSequenceFromMask((
    '[#84018 ]', ), ), name='Set-5')
mdb.models['Model-1'].parts['Parts'].SectionAssignment(offset=0.0, offsetField=
    '', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Parts'].sets['Set-5'], sectionName='Section-2'
    , thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Parts'].Set(cells=
    mdb.models['Model-1'].parts['Parts'].cells.getSequenceFromMask(('[#3800 ]',
    ), ), name='Set-6')
mdb.models['Model-1'].parts['Parts'].SectionAssignment(offset=0.0, offsetField=
    '', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Parts'].sets['Set-6'], sectionName='Section-1'
    , thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Parts'].Set(cells=
    mdb.models['Model-1'].parts['Parts'].cells.getSequenceFromMask((
    '[#20000 ]', ), ), name='Set-3')
mdb.models['Model-1'].parts['Parts'].Set(cells=
    mdb.models['Model-1'].parts['Parts'].cells.getSequenceFromMask(('[#481 ]',
    ), ), name='Set-7')
mdb.models['Model-1'].parts['Parts'].SectionAssignment(offset=0.0, offsetField=
    '', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Parts'].sets['Set-7'], sectionName='Section-1'
    , thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Parts'].Set(cells=
    mdb.models['Model-1'].parts['Parts'].cells.getSequenceFromMask(('[#6 ]', ),
    ), name='Set-8')
mdb.models['Model-1'].parts['Parts'].SectionAssignment(offset=0.0, offsetField=
    '', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Parts'].sets['Set-8'], sectionName='Section-1'
    , thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Parts'].Set(cells=
    mdb.models['Model-1'].parts['Parts'].cells.getSequenceFromMask(('[#360 ]',
    ), ), name='Set-9')
mdb.models['Model-1'].parts['Parts'].SectionAssignment(offset=0.0, offsetField=
    '', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Parts'].sets['Set-9'], sectionName='Section-2'
    , thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Parts'].sectionAssignments[4].setValues(
    sectionName='Section-1')
# Save by jiaor on 2022_05_02-14.43.34; build 2021 2020_03_06-22.50.37 167380
from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *
mdb.models['Model-1'].rootAssembly.DatumCsysByDefault(CARTESIAN)
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Parts-1', part=
    mdb.models['Model-1'].parts['Parts'])
mdb.models['Model-1'].StaticStep(initialInc=0.005, maxInc=0.1, maxNumInc=1000,
    name='Step-1', nlgeom=ON, previous='Initial')
mdb.models['Model-1'].PinnedBC(createStepName='Step-1', localCsys=None, name=
    'BC-1', region=
    mdb.models['Model-1'].rootAssembly.instances['Parts-1'].sets['Set-1'])
mdb.models['Model-1'].PinnedBC(createStepName='Step-1', localCsys=None, name=
    'BC-2', region=
    mdb.models['Model-1'].rootAssembly.instances['Parts-1'].sets['Set-2'])
mdb.models['Model-1'].PinnedBC(createStepName='Step-1', localCsys=None, name=
    'BC-3', region=
    mdb.models['Model-1'].rootAssembly.instances['Parts-1'].sets['Set-3'])
mdb.models['Model-1'].PinnedBC(createStepName='Step-1', localCsys=None, name=
    'BC-4', region=
    mdb.models['Model-1'].rootAssembly.instances['Parts-1'].sets['Set-4'])
mdb.models['Model-1'].rootAssembly.Surface(name='Surf-1', side1Faces=
    mdb.models['Model-1'].rootAssembly.instances['Parts-1'].faces.getSequenceFromMask(
    ('[#8894248a #1022222 #439e7f80 ]', ), ))
mdb.models['Model-1'].Pressure(amplitude=UNSET, createStepName='Step-1',
    distributionType=UNIFORM, field='', magnitude=500.0, name='Load-1', region=
    mdb.models['Model-1'].rootAssembly.surfaces['Surf-1'])
mdb.models['Model-1'].parts['Parts'].seedPart(deviationFactor=0.1,
    minSizeFactor=0.1, size=1.0)
mdb.models['Model-1'].parts['Parts'].generateMesh()
mdb.models['Model-1'].rootAssembly.regenerate()
mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF,
    explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF,
    memory=90, memoryUnits=PERCENTAGE, model='Model-1', modelPrint=OFF,
    multiprocessingMode=DEFAULT, name='Job-1', nodalOutputPrecision=SINGLE,
    numCpus=1, numGPUs=0, queue=None, resultsFormat=ODB, scratch='', type=
    ANALYSIS, userSubroutine='', waitHours=0, waitMinutes=0)
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
mdb.jobs['Job-1']._Message(STARTED, {'phase': BATCHPRE_PHASE,
    'clientHost': 'DESKTOP-HP', 'handle': 0, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(ODB_FILE, {'phase': BATCHPRE_PHASE,
    'file': 'C:\\Users\\jiaor\\Desktop\\Job-1.odb', 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(COMPLETED, {'phase': BATCHPRE_PHASE,
    'message': 'Analysis phase complete', 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(STARTED, {'phase': STANDARD_PHASE,
    'clientHost': 'DESKTOP-HP', 'handle': 17392, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(STEP, {'phase': STANDARD_PHASE, 'stepId': 1,
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 0, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(MEMORY_ESTIMATE, {'phase': STANDARD_PHASE,
    'jobName': 'Job-1', 'memory': 185.0})
mdb.jobs['Job-1']._Message(PHYSICAL_MEMORY, {'phase': STANDARD_PHASE,
    'physical_memory': 16106.0, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(MINIMUM_MEMORY, {'minimum_memory': 41.0,
    'phase': STANDARD_PHASE, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 1, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(STATUS, {'totalTime': 0.005, 'attempts': 1,
    'timeIncrement': 0.005, 'increment': 1, 'stepTime': 0.005, 'step': 1,
    'jobName': 'Job-1', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE,
    'equilibrium': 1})
mdb.jobs['Job-1']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 2, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(STATUS, {'totalTime': 0.01, 'attempts': 1,
    'timeIncrement': 0.005, 'increment': 2, 'stepTime': 0.01, 'step': 1,
    'jobName': 'Job-1', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE,
    'equilibrium': 1})
mdb.jobs['Job-1']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 3, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(STATUS, {'totalTime': 0.0175, 'attempts': 1,
    'timeIncrement': 0.0075, 'increment': 3, 'stepTime': 0.0175, 'step': 1,
    'jobName': 'Job-1', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE,
    'equilibrium': 1})
mdb.jobs['Job-1']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 4, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(STATUS, {'totalTime': 0.02875, 'attempts': 1,
    'timeIncrement': 0.01125, 'increment': 4, 'stepTime': 0.02875, 'step': 1,
    'jobName': 'Job-1', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE,
    'equilibrium': 1})
mdb.jobs['Job-1']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 5, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(STATUS, {'totalTime': 0.045625, 'attempts': 1,
    'timeIncrement': 0.016875, 'increment': 5, 'stepTime': 0.045625, 'step': 1,
    'jobName': 'Job-1', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE,
    'equilibrium': 1})
mdb.jobs['Job-1']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 6, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(STATUS, {'totalTime': 0.0709375, 'attempts': 1,
    'timeIncrement': 0.0253125, 'increment': 6, 'stepTime': 0.0709375,
    'step': 1, 'jobName': 'Job-1', 'severe': 0, 'iterations': 1,
    'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['Job-1']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 7, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(STATUS, {'totalTime': 0.10890625, 'attempts': 1,
    'timeIncrement': 0.03796875, 'increment': 7, 'stepTime': 0.10890625,
    'step': 1, 'jobName': 'Job-1', 'severe': 0, 'iterations': 1,
    'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['Job-1']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 8, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(STATUS, {'totalTime': 0.165859375, 'attempts': 1,
    'timeIncrement': 0.056953125, 'increment': 8, 'stepTime': 0.165859375,
    'step': 1, 'jobName': 'Job-1', 'severe': 0, 'iterations': 1,
    'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['Job-1']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 9, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(STATUS, {'totalTime': 0.2512890625, 'attempts': 1,
    'timeIncrement': 0.0854296875, 'increment': 9, 'stepTime': 0.2512890625,
    'step': 1, 'jobName': 'Job-1', 'severe': 0, 'iterations': 1,
    'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['Job-1']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 10, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(STATUS, {'totalTime': 0.3512890625, 'attempts': 1,
    'timeIncrement': 0.1, 'increment': 10, 'stepTime': 0.3512890625, 'step': 1,
    'jobName': 'Job-1', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE,
    'equilibrium': 1})
mdb.jobs['Job-1']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 11, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(STATUS, {'totalTime': 0.4512890625, 'attempts': 1,
    'timeIncrement': 0.1, 'increment': 11, 'stepTime': 0.4512890625, 'step': 1,
    'jobName': 'Job-1', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE,
    'equilibrium': 1})
mdb.jobs['Job-1']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 12, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(STATUS, {'totalTime': 0.5512890625, 'attempts': 1,
    'timeIncrement': 0.1, 'increment': 12, 'stepTime': 0.5512890625, 'step': 1,
    'jobName': 'Job-1', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE,
    'equilibrium': 1})
mdb.jobs['Job-1']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 13, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(STATUS, {'totalTime': 0.6512890625, 'attempts': 1,
    'timeIncrement': 0.1, 'increment': 13, 'stepTime': 0.6512890625, 'step': 1,
    'jobName': 'Job-1', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE,
    'equilibrium': 1})
mdb.jobs['Job-1']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 14, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(STATUS, {'totalTime': 0.7512890625, 'attempts': 1,
    'timeIncrement': 0.1, 'increment': 14, 'stepTime': 0.7512890625, 'step': 1,
    'jobName': 'Job-1', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE,
    'equilibrium': 1})
mdb.jobs['Job-1']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 15, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(STATUS, {'totalTime': 0.8512890625, 'attempts': 1,
    'timeIncrement': 0.1, 'increment': 15, 'stepTime': 0.8512890625, 'step': 1,
    'jobName': 'Job-1', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE,
    'equilibrium': 1})
mdb.jobs['Job-1']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 16, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(STATUS, {'totalTime': 0.9512890625, 'attempts': 1,
    'timeIncrement': 0.1, 'increment': 16, 'stepTime': 0.9512890625, 'step': 1,
    'jobName': 'Job-1', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE,
    'equilibrium': 1})
mdb.jobs['Job-1']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 17, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(STATUS, {'totalTime': 1.0, 'attempts': 1,
    'timeIncrement': 0.0487109375000001, 'increment': 17, 'stepTime': 1.0,
    'step': 1, 'jobName': 'Job-1', 'severe': 0, 'iterations': 1,
    'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['Job-1']._Message(END_STEP, {'phase': STANDARD_PHASE, 'stepId': 1,
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(COMPLETED, {'phase': STANDARD_PHASE,
    'message': 'Analysis phase complete', 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(JOB_COMPLETED, {'time': 'Mon May  2 14:47:39 2022',
    'jobName': 'Job-1'})
mdb.models['Model-1'].parts['Parts'].sectionAssignments[4].setValues(
    sectionName='Section-2')
mdb.models['Model-1'].parts['Parts'].generateMesh()
mdb.models['Model-1'].rootAssembly.regenerate()
mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF,
    explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF,
    memory=90, memoryUnits=PERCENTAGE, model='Model-1', modelPrint=OFF,
    multiprocessingMode=DEFAULT, name='Job-2', nodalOutputPrecision=SINGLE,
    numCpus=1, numGPUs=0, queue=None, resultsFormat=ODB, scratch='', type=
    ANALYSIS, userSubroutine='', waitHours=0, waitMinutes=0)
mdb.jobs['Job-2'].submit(consistencyChecking=OFF)
mdb.jobs['Job-2']._Message(STARTED, {'phase': BATCHPRE_PHASE,
    'clientHost': 'DESKTOP-HP', 'handle': 0, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(ODB_FILE, {'phase': BATCHPRE_PHASE,
    'file': 'C:\\Users\\jiaor\\Desktop\\Job-2.odb', 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(COMPLETED, {'phase': BATCHPRE_PHASE,
    'message': 'Analysis phase complete', 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(STARTED, {'phase': STANDARD_PHASE,
    'clientHost': 'DESKTOP-HP', 'handle': 19888, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(STEP, {'phase': STANDARD_PHASE, 'stepId': 1,
    'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 0, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(MEMORY_ESTIMATE, {'phase': STANDARD_PHASE,
    'jobName': 'Job-2', 'memory': 185.0})
mdb.jobs['Job-2']._Message(PHYSICAL_MEMORY, {'phase': STANDARD_PHASE,
    'physical_memory': 16106.0, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(MINIMUM_MEMORY, {'minimum_memory': 41.0,
    'phase': STANDARD_PHASE, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 1, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(STATUS, {'totalTime': 0.005, 'attempts': 1,
    'timeIncrement': 0.005, 'increment': 1, 'stepTime': 0.005, 'step': 1,
    'jobName': 'Job-2', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE,
    'equilibrium': 1})
mdb.jobs['Job-2']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 2, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(STATUS, {'totalTime': 0.01, 'attempts': 1,
    'timeIncrement': 0.005, 'increment': 2, 'stepTime': 0.01, 'step': 1,
    'jobName': 'Job-2', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE,
    'equilibrium': 1})
mdb.jobs['Job-2']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 3, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(STATUS, {'totalTime': 0.0175, 'attempts': 1,
    'timeIncrement': 0.0075, 'increment': 3, 'stepTime': 0.0175, 'step': 1,
    'jobName': 'Job-2', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE,
    'equilibrium': 1})
mdb.jobs['Job-2']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 4, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(STATUS, {'totalTime': 0.02875, 'attempts': 1,
    'timeIncrement': 0.01125, 'increment': 4, 'stepTime': 0.02875, 'step': 1,
    'jobName': 'Job-2', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE,
    'equilibrium': 1})
mdb.jobs['Job-2']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 5, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(STATUS, {'totalTime': 0.045625, 'attempts': 1,
    'timeIncrement': 0.016875, 'increment': 5, 'stepTime': 0.045625, 'step': 1,
    'jobName': 'Job-2', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE,
    'equilibrium': 1})
mdb.jobs['Job-2']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 6, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(STATUS, {'totalTime': 0.0709375, 'attempts': 1,
    'timeIncrement': 0.0253125, 'increment': 6, 'stepTime': 0.0709375,
    'step': 1, 'jobName': 'Job-2', 'severe': 0, 'iterations': 1,
    'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['Job-2']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 7, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(STATUS, {'totalTime': 0.10890625, 'attempts': 1,
    'timeIncrement': 0.03796875, 'increment': 7, 'stepTime': 0.10890625,
    'step': 1, 'jobName': 'Job-2', 'severe': 0, 'iterations': 1,
    'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['Job-2']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 8, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(STATUS, {'totalTime': 0.165859375, 'attempts': 1,
    'timeIncrement': 0.056953125, 'increment': 8, 'stepTime': 0.165859375,
    'step': 1, 'jobName': 'Job-2', 'severe': 0, 'iterations': 1,
    'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['Job-2']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 9, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(STATUS, {'totalTime': 0.2512890625, 'attempts': 1,
    'timeIncrement': 0.0854296875, 'increment': 9, 'stepTime': 0.2512890625,
    'step': 1, 'jobName': 'Job-2', 'severe': 0, 'iterations': 1,
    'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['Job-2']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 10, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(STATUS, {'totalTime': 0.3512890625, 'attempts': 1,
    'timeIncrement': 0.1, 'increment': 10, 'stepTime': 0.3512890625, 'step': 1,
    'jobName': 'Job-2', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE,
    'equilibrium': 1})
mdb.jobs['Job-2']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 11, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(STATUS, {'totalTime': 0.4512890625, 'attempts': 1,
    'timeIncrement': 0.1, 'increment': 11, 'stepTime': 0.4512890625, 'step': 1,
    'jobName': 'Job-2', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE,
    'equilibrium': 1})
mdb.jobs['Job-2']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 12, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(STATUS, {'totalTime': 0.5512890625, 'attempts': 1,
    'timeIncrement': 0.1, 'increment': 12, 'stepTime': 0.5512890625, 'step': 1,
    'jobName': 'Job-2', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE,
    'equilibrium': 1})
mdb.jobs['Job-2']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 13, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(STATUS, {'totalTime': 0.6512890625, 'attempts': 1,
    'timeIncrement': 0.1, 'increment': 13, 'stepTime': 0.6512890625, 'step': 1,
    'jobName': 'Job-2', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE,
    'equilibrium': 1})
mdb.jobs['Job-2']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 14, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(STATUS, {'totalTime': 0.7512890625, 'attempts': 1,
    'timeIncrement': 0.1, 'increment': 14, 'stepTime': 0.7512890625, 'step': 1,
    'jobName': 'Job-2', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE,
    'equilibrium': 1})
mdb.jobs['Job-2']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 15, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(STATUS, {'totalTime': 0.8512890625, 'attempts': 1,
    'timeIncrement': 0.1, 'increment': 15, 'stepTime': 0.8512890625, 'step': 1,
    'jobName': 'Job-2', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE,
    'equilibrium': 1})
mdb.jobs['Job-2']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 16, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(STATUS, {'totalTime': 0.9512890625, 'attempts': 1,
    'timeIncrement': 0.1, 'increment': 16, 'stepTime': 0.9512890625, 'step': 1,
    'jobName': 'Job-2', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE,
    'equilibrium': 1})
mdb.jobs['Job-2']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 17, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(STATUS, {'totalTime': 1.0, 'attempts': 1,
    'timeIncrement': 0.0487109375000001, 'increment': 17, 'stepTime': 1.0,
    'step': 1, 'jobName': 'Job-2', 'severe': 0, 'iterations': 1,
    'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['Job-2']._Message(END_STEP, {'phase': STANDARD_PHASE, 'stepId': 1,
    'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(COMPLETED, {'phase': STANDARD_PHASE,
    'message': 'Analysis phase complete', 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(JOB_COMPLETED, {'time': 'Mon May  2 14:51:38 2022',
    'jobName': 'Job-2'})
del mdb.models['Model-1'].parts['Parts'].sectionAssignments[4]
del mdb.models['Model-1'].parts['Parts'].sectionAssignments[5]
del mdb.models['Model-1'].parts['Parts'].sectionAssignments[6]
del mdb.models['Model-1'].parts['Parts'].sectionAssignments[5]
del mdb.models['Model-1'].parts['Parts'].sectionAssignments[4]
# Save by jiaor on 2022_05_02-14.53.09; build 2021 2020_03_06-22.50.37 167380
from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *
mdb.models['Model-1'].parts['Parts'].Set(cells=
    mdb.models['Model-1'].parts['Parts'].cells.getSequenceFromMask(('[#613f ]',
    ), ), name='Set-10')
mdb.models['Model-1'].parts['Parts'].SectionAssignment(offset=0.0, offsetField=
    '', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Parts'].sets['Set-10'], sectionName=
    'Section-2', thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Parts'].Set(cells=
    mdb.models['Model-1'].parts['Parts'].cells.getSequenceFromMask((
    '[#81ec0 ]', ), ), name='Set-11')
mdb.models['Model-1'].parts['Parts'].SectionAssignment(offset=0.0, offsetField=
    '', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Parts'].sets['Set-11'], sectionName=
    'Section-1', thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Parts'].deleteMesh()
mdb.models['Model-1'].parts['Parts'].seedPart(deviationFactor=0.1,
    minSizeFactor=0.1, size=2.0)
mdb.models['Model-1'].parts['Parts'].generateMesh()
mdb.models['Model-1'].rootAssembly.regenerate()
mdb.jobs['Job-2'].submit(consistencyChecking=OFF)
mdb.jobs['Job-2']._Message(STARTED, {'phase': BATCHPRE_PHASE,
    'clientHost': 'DESKTOP-HP', 'handle': 0, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(ODB_FILE, {'phase': BATCHPRE_PHASE,
    'file': 'C:\\Users\\jiaor\\Desktop\\Job-2.odb', 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(COMPLETED, {'phase': BATCHPRE_PHASE,
    'message': 'Analysis phase complete', 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(STARTED, {'phase': STANDARD_PHASE,
    'clientHost': 'DESKTOP-HP', 'handle': 8756, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(STEP, {'phase': STANDARD_PHASE, 'stepId': 1,
    'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 0, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(MEMORY_ESTIMATE, {'phase': STANDARD_PHASE,
    'jobName': 'Job-2', 'memory': 58.0})
mdb.jobs['Job-2']._Message(PHYSICAL_MEMORY, {'phase': STANDARD_PHASE,
    'physical_memory': 16106.0, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(MINIMUM_MEMORY, {'minimum_memory': 20.0,
    'phase': STANDARD_PHASE, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 1, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(STATUS, {'totalTime': 0.005, 'attempts': 1,
    'timeIncrement': 0.005, 'increment': 1, 'stepTime': 0.005, 'step': 1,
    'jobName': 'Job-2', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE,
    'equilibrium': 1})
mdb.jobs['Job-2']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 2, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(STATUS, {'totalTime': 0.01, 'attempts': 1,
    'timeIncrement': 0.005, 'increment': 2, 'stepTime': 0.01, 'step': 1,
    'jobName': 'Job-2', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE,
    'equilibrium': 1})
mdb.jobs['Job-2']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 3, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(STATUS, {'totalTime': 0.0175, 'attempts': 1,
    'timeIncrement': 0.0075, 'increment': 3, 'stepTime': 0.0175, 'step': 1,
    'jobName': 'Job-2', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE,
    'equilibrium': 1})
mdb.jobs['Job-2']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 4, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(STATUS, {'totalTime': 0.02875, 'attempts': 1,
    'timeIncrement': 0.01125, 'increment': 4, 'stepTime': 0.02875, 'step': 1,
    'jobName': 'Job-2', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE,
    'equilibrium': 1})
mdb.jobs['Job-2']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 5, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(STATUS, {'totalTime': 0.045625, 'attempts': 1,
    'timeIncrement': 0.016875, 'increment': 5, 'stepTime': 0.045625, 'step': 1,
    'jobName': 'Job-2', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE,
    'equilibrium': 1})
mdb.jobs['Job-2']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 6, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(STATUS, {'totalTime': 0.0709375, 'attempts': 1,
    'timeIncrement': 0.0253125, 'increment': 6, 'stepTime': 0.0709375,
    'step': 1, 'jobName': 'Job-2', 'severe': 0, 'iterations': 1,
    'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['Job-2']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 7, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(STATUS, {'totalTime': 0.10890625, 'attempts': 1,
    'timeIncrement': 0.03796875, 'increment': 7, 'stepTime': 0.10890625,
    'step': 1, 'jobName': 'Job-2', 'severe': 0, 'iterations': 1,
    'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['Job-2']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 8, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(STATUS, {'totalTime': 0.165859375, 'attempts': 1,
    'timeIncrement': 0.056953125, 'increment': 8, 'stepTime': 0.165859375,
    'step': 1, 'jobName': 'Job-2', 'severe': 0, 'iterations': 1,
    'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['Job-2']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 9, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(STATUS, {'totalTime': 0.2512890625, 'attempts': 1,
    'timeIncrement': 0.0854296875, 'increment': 9, 'stepTime': 0.2512890625,
    'step': 1, 'jobName': 'Job-2', 'severe': 0, 'iterations': 1,
    'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['Job-2']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 10, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(STATUS, {'totalTime': 0.3512890625, 'attempts': 1,
    'timeIncrement': 0.1, 'increment': 10, 'stepTime': 0.3512890625, 'step': 1,
    'jobName': 'Job-2', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE,
    'equilibrium': 1})
mdb.jobs['Job-2']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 11, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(STATUS, {'totalTime': 0.4512890625, 'attempts': 1,
    'timeIncrement': 0.1, 'increment': 11, 'stepTime': 0.4512890625, 'step': 1,
    'jobName': 'Job-2', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE,
    'equilibrium': 1})
mdb.jobs['Job-2']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 12, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(STATUS, {'totalTime': 0.5512890625, 'attempts': 1,
    'timeIncrement': 0.1, 'increment': 12, 'stepTime': 0.5512890625, 'step': 1,
    'jobName': 'Job-2', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE,
    'equilibrium': 1})
mdb.jobs['Job-2']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 13, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(STATUS, {'totalTime': 0.6512890625, 'attempts': 1,
    'timeIncrement': 0.1, 'increment': 13, 'stepTime': 0.6512890625, 'step': 1,
    'jobName': 'Job-2', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE,
    'equilibrium': 1})
mdb.jobs['Job-2']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 14, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(STATUS, {'totalTime': 0.7512890625, 'attempts': 1,
    'timeIncrement': 0.1, 'increment': 14, 'stepTime': 0.7512890625, 'step': 1,
    'jobName': 'Job-2', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE,
    'equilibrium': 1})
mdb.jobs['Job-2']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 15, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(STATUS, {'totalTime': 0.8512890625, 'attempts': 1,
    'timeIncrement': 0.1, 'increment': 15, 'stepTime': 0.8512890625, 'step': 1,
    'jobName': 'Job-2', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE,
    'equilibrium': 1})
mdb.jobs['Job-2']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 16, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(STATUS, {'totalTime': 0.9512890625, 'attempts': 1,
    'timeIncrement': 0.1, 'increment': 16, 'stepTime': 0.9512890625, 'step': 1,
    'jobName': 'Job-2', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE,
    'equilibrium': 1})
mdb.jobs['Job-2']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 17, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(STATUS, {'totalTime': 1.0, 'attempts': 1,
    'timeIncrement': 0.0487109375000001, 'increment': 17, 'stepTime': 1.0,
    'step': 1, 'jobName': 'Job-2', 'severe': 0, 'iterations': 1,
    'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['Job-2']._Message(END_STEP, {'phase': STANDARD_PHASE, 'stepId': 1,
    'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(COMPLETED, {'phase': STANDARD_PHASE,
    'message': 'Analysis phase complete', 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(JOB_COMPLETED, {'time': 'Mon May  2 14:55:40 2022',
    'jobName': 'Job-2'})
# Save by jiaor on 2022_05_02-14.57.09; build 2021 2020_03_06-22.50.37 167380
# Save by jiaor on 2022_05_02-14.57.32; build 2021 2020_03_06-22.50.37 167380
# Save by jiaor on 2022_05_02-15.04.43; build 2021 2020_03_06-22.50.37 167380
from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *
del mdb.models['Model-1'].parts['Parts'].sectionAssignments[5]
del mdb.models['Model-1'].parts['Parts'].sectionAssignments[4]
mdb.models['Model-1'].parts['Parts'].Set(cells=
    mdb.models['Model-1'].parts['Parts'].cells.getSequenceFromMask(('[#320 ]',
    ), ), name='Set-12')
mdb.models['Model-1'].parts['Parts'].SectionAssignment(offset=0.0, offsetField=
    '', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Parts'].sets['Set-12'], sectionName=
    'Section-1', thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Parts'].Set(cells=
    mdb.models['Model-1'].parts['Parts'].cells.getSequenceFromMask((
    '[#87cdf ]', ), ), name='Set-13')
mdb.models['Model-1'].parts['Parts'].SectionAssignment(offset=0.0, offsetField=
    '', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Parts'].sets['Set-13'], sectionName=
    'Section-2', thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].rootAssembly.regenerate()
# Save by jiaor on 2022_05_02-15.06.19; build 2021 2020_03_06-22.50.37 167380
from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *
mdb.models['Model-1'].loads['Load-1'].setValues(magnitude=1000.0)
# Save by jiaor on 2022_05_02-15.06.41; build 2021 2020_03_06-22.50.37 167380
from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *
mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF,
    explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF,
    memory=90, memoryUnits=PERCENTAGE, model='Model-1', modelPrint=OFF,
    multiprocessingMode=DEFAULT, name='Job-3', nodalOutputPrecision=SINGLE,
    numCpus=1, numGPUs=0, queue=None, resultsFormat=ODB, scratch='', type=
    ANALYSIS, userSubroutine='', waitHours=0, waitMinutes=0)
mdb.jobs['Job-3'].submit(consistencyChecking=OFF)
mdb.jobs['Job-3']._Message(STARTED, {'phase': BATCHPRE_PHASE,
    'clientHost': 'DESKTOP-HP', 'handle': 0, 'jobName': 'Job-3'})
mdb.jobs['Job-3']._Message(ODB_FILE, {'phase': BATCHPRE_PHASE,
    'file': 'C:\\Users\\jiaor\\Desktop\\Job-3.odb', 'jobName': 'Job-3'})
mdb.jobs['Job-3']._Message(COMPLETED, {'phase': BATCHPRE_PHASE,
    'message': 'Analysis phase complete', 'jobName': 'Job-3'})
mdb.jobs['Job-3']._Message(STARTED, {'phase': STANDARD_PHASE,
    'clientHost': 'DESKTOP-HP', 'handle': 20364, 'jobName': 'Job-3'})
mdb.jobs['Job-3']._Message(STEP, {'phase': STANDARD_PHASE, 'stepId': 1,
    'jobName': 'Job-3'})
mdb.jobs['Job-3']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 0, 'jobName': 'Job-3'})
mdb.jobs['Job-3']._Message(MEMORY_ESTIMATE, {'phase': STANDARD_PHASE,
    'jobName': 'Job-3', 'memory': 58.0})
mdb.jobs['Job-3']._Message(PHYSICAL_MEMORY, {'phase': STANDARD_PHASE,
    'physical_memory': 16106.0, 'jobName': 'Job-3'})
mdb.jobs['Job-3']._Message(MINIMUM_MEMORY, {'minimum_memory': 20.0,
    'phase': STANDARD_PHASE, 'jobName': 'Job-3'})
mdb.jobs['Job-3']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 1, 'jobName': 'Job-3'})
mdb.jobs['Job-3']._Message(STATUS, {'totalTime': 0.005, 'attempts': 1,
    'timeIncrement': 0.005, 'increment': 1, 'stepTime': 0.005, 'step': 1,
    'jobName': 'Job-3', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE,
    'equilibrium': 1})
mdb.jobs['Job-3']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 2, 'jobName': 'Job-3'})
mdb.jobs['Job-3']._Message(STATUS, {'totalTime': 0.01, 'attempts': 1,
    'timeIncrement': 0.005, 'increment': 2, 'stepTime': 0.01, 'step': 1,
    'jobName': 'Job-3', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE,
    'equilibrium': 1})
mdb.jobs['Job-3']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 3, 'jobName': 'Job-3'})
mdb.jobs['Job-3']._Message(STATUS, {'totalTime': 0.0175, 'attempts': 1,
    'timeIncrement': 0.0075, 'increment': 3, 'stepTime': 0.0175, 'step': 1,
    'jobName': 'Job-3', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE,
    'equilibrium': 1})
mdb.jobs['Job-3']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 4, 'jobName': 'Job-3'})
mdb.jobs['Job-3']._Message(STATUS, {'totalTime': 0.02875, 'attempts': 1,
    'timeIncrement': 0.01125, 'increment': 4, 'stepTime': 0.02875, 'step': 1,
    'jobName': 'Job-3', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE,
    'equilibrium': 1})
mdb.jobs['Job-3']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 5, 'jobName': 'Job-3'})
mdb.jobs['Job-3']._Message(STATUS, {'totalTime': 0.045625, 'attempts': 1,
    'timeIncrement': 0.016875, 'increment': 5, 'stepTime': 0.045625, 'step': 1,
    'jobName': 'Job-3', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE,
    'equilibrium': 1})
mdb.jobs['Job-3']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 6, 'jobName': 'Job-3'})
mdb.jobs['Job-3']._Message(STATUS, {'totalTime': 0.0709375, 'attempts': 1,
    'timeIncrement': 0.0253125, 'increment': 6, 'stepTime': 0.0709375,
    'step': 1, 'jobName': 'Job-3', 'severe': 0, 'iterations': 1,
    'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['Job-3']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 7, 'jobName': 'Job-3'})
mdb.jobs['Job-3']._Message(STATUS, {'totalTime': 0.10890625, 'attempts': 1,
    'timeIncrement': 0.03796875, 'increment': 7, 'stepTime': 0.10890625,
    'step': 1, 'jobName': 'Job-3', 'severe': 0, 'iterations': 1,
    'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['Job-3']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 8, 'jobName': 'Job-3'})
mdb.jobs['Job-3']._Message(STATUS, {'totalTime': 0.165859375, 'attempts': 1,
    'timeIncrement': 0.056953125, 'increment': 8, 'stepTime': 0.165859375,
    'step': 1, 'jobName': 'Job-3', 'severe': 0, 'iterations': 1,
    'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['Job-3']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 9, 'jobName': 'Job-3'})
mdb.jobs['Job-3']._Message(STATUS, {'totalTime': 0.2512890625, 'attempts': 1,
    'timeIncrement': 0.0854296875, 'increment': 9, 'stepTime': 0.2512890625,
    'step': 1, 'jobName': 'Job-3', 'severe': 0, 'iterations': 1,
    'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['Job-3']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 10, 'jobName': 'Job-3'})
mdb.jobs['Job-3']._Message(STATUS, {'totalTime': 0.3512890625, 'attempts': 1,
    'timeIncrement': 0.1, 'increment': 10, 'stepTime': 0.3512890625, 'step': 1,
    'jobName': 'Job-3', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE,
    'equilibrium': 1})
mdb.jobs['Job-3']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 11, 'jobName': 'Job-3'})
mdb.jobs['Job-3']._Message(STATUS, {'totalTime': 0.4512890625, 'attempts': 1,
    'timeIncrement': 0.1, 'increment': 11, 'stepTime': 0.4512890625, 'step': 1,
    'jobName': 'Job-3', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE,
    'equilibrium': 1})
mdb.jobs['Job-3']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 12, 'jobName': 'Job-3'})
mdb.jobs['Job-3']._Message(STATUS, {'totalTime': 0.5512890625, 'attempts': 1,
    'timeIncrement': 0.1, 'increment': 12, 'stepTime': 0.5512890625, 'step': 1,
    'jobName': 'Job-3', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE,
    'equilibrium': 1})
mdb.jobs['Job-3']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 13, 'jobName': 'Job-3'})
mdb.jobs['Job-3']._Message(STATUS, {'totalTime': 0.6512890625, 'attempts': 1,
    'timeIncrement': 0.1, 'increment': 13, 'stepTime': 0.6512890625, 'step': 1,
    'jobName': 'Job-3', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE,
    'equilibrium': 1})
mdb.jobs['Job-3']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 14, 'jobName': 'Job-3'})
mdb.jobs['Job-3']._Message(STATUS, {'totalTime': 0.7512890625, 'attempts': 1,
    'timeIncrement': 0.1, 'increment': 14, 'stepTime': 0.7512890625, 'step': 1,
    'jobName': 'Job-3', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE,
    'equilibrium': 1})
mdb.jobs['Job-3']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 15, 'jobName': 'Job-3'})
mdb.jobs['Job-3']._Message(STATUS, {'totalTime': 0.8512890625, 'attempts': 1,
    'timeIncrement': 0.1, 'increment': 15, 'stepTime': 0.8512890625, 'step': 1,
    'jobName': 'Job-3', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE,
    'equilibrium': 1})
mdb.jobs['Job-3']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 16, 'jobName': 'Job-3'})
mdb.jobs['Job-3']._Message(STATUS, {'totalTime': 0.9512890625, 'attempts': 1,
    'timeIncrement': 0.1, 'increment': 16, 'stepTime': 0.9512890625, 'step': 1,
    'jobName': 'Job-3', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE,
    'equilibrium': 1})
mdb.jobs['Job-3']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 17, 'jobName': 'Job-3'})
mdb.jobs['Job-3']._Message(STATUS, {'totalTime': 1.0, 'attempts': 1,
    'timeIncrement': 0.0487109375000001, 'increment': 17, 'stepTime': 1.0,
    'step': 1, 'jobName': 'Job-3', 'severe': 0, 'iterations': 1,
    'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['Job-3']._Message(END_STEP, {'phase': STANDARD_PHASE, 'stepId': 1,
    'jobName': 'Job-3'})
mdb.jobs['Job-3']._Message(COMPLETED, {'phase': STANDARD_PHASE,
    'message': 'Analysis phase complete', 'jobName': 'Job-3'})
mdb.jobs['Job-3']._Message(JOB_COMPLETED, {'time': 'Mon May  2 15:07:18 2022',
    'jobName': 'Job-3'})
mdb.models['Model-1'].loads['Load-1'].setValues(magnitude=500.0)
mdb.jobs['Job-3'].submit(consistencyChecking=OFF)
mdb.jobs['Job-3']._Message(STARTED, {'phase': BATCHPRE_PHASE,
    'clientHost': 'DESKTOP-HP', 'handle': 0, 'jobName': 'Job-3'})
mdb.jobs['Job-3']._Message(ODB_FILE, {'phase': BATCHPRE_PHASE,
    'file': 'C:\\Users\\jiaor\\Desktop\\Job-3.odb', 'jobName': 'Job-3'})
mdb.jobs['Job-3']._Message(COMPLETED, {'phase': BATCHPRE_PHASE,
    'message': 'Analysis phase complete', 'jobName': 'Job-3'})
mdb.jobs['Job-3']._Message(STARTED, {'phase': STANDARD_PHASE,
    'clientHost': 'DESKTOP-HP', 'handle': 9356, 'jobName': 'Job-3'})
mdb.jobs['Job-3']._Message(STEP, {'phase': STANDARD_PHASE, 'stepId': 1,
    'jobName': 'Job-3'})
mdb.jobs['Job-3']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 0, 'jobName': 'Job-3'})
mdb.jobs['Job-3']._Message(MEMORY_ESTIMATE, {'phase': STANDARD_PHASE,
    'jobName': 'Job-3', 'memory': 58.0})
mdb.jobs['Job-3']._Message(PHYSICAL_MEMORY, {'phase': STANDARD_PHASE,
    'physical_memory': 16106.0, 'jobName': 'Job-3'})
mdb.jobs['Job-3']._Message(MINIMUM_MEMORY, {'minimum_memory': 20.0,
    'phase': STANDARD_PHASE, 'jobName': 'Job-3'})
mdb.jobs['Job-3']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 1, 'jobName': 'Job-3'})
mdb.jobs['Job-3']._Message(STATUS, {'totalTime': 0.005, 'attempts': 1,
    'timeIncrement': 0.005, 'increment': 1, 'stepTime': 0.005, 'step': 1,
    'jobName': 'Job-3', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE,
    'equilibrium': 1})
mdb.jobs['Job-3']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 2, 'jobName': 'Job-3'})
mdb.jobs['Job-3']._Message(STATUS, {'totalTime': 0.01, 'attempts': 1,
    'timeIncrement': 0.005, 'increment': 2, 'stepTime': 0.01, 'step': 1,
    'jobName': 'Job-3', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE,
    'equilibrium': 1})
mdb.jobs['Job-3']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 3, 'jobName': 'Job-3'})
mdb.jobs['Job-3']._Message(STATUS, {'totalTime': 0.0175, 'attempts': 1,
    'timeIncrement': 0.0075, 'increment': 3, 'stepTime': 0.0175, 'step': 1,
    'jobName': 'Job-3', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE,
    'equilibrium': 1})
mdb.jobs['Job-3']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 4, 'jobName': 'Job-3'})
mdb.jobs['Job-3']._Message(STATUS, {'totalTime': 0.02875, 'attempts': 1,
    'timeIncrement': 0.01125, 'increment': 4, 'stepTime': 0.02875, 'step': 1,
    'jobName': 'Job-3', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE,
    'equilibrium': 1})
mdb.jobs['Job-3']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 5, 'jobName': 'Job-3'})
mdb.jobs['Job-3']._Message(STATUS, {'totalTime': 0.045625, 'attempts': 1,
    'timeIncrement': 0.016875, 'increment': 5, 'stepTime': 0.045625, 'step': 1,
    'jobName': 'Job-3', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE,
    'equilibrium': 1})
mdb.jobs['Job-3']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 6, 'jobName': 'Job-3'})
mdb.jobs['Job-3']._Message(STATUS, {'totalTime': 0.0709375, 'attempts': 1,
    'timeIncrement': 0.0253125, 'increment': 6, 'stepTime': 0.0709375,
    'step': 1, 'jobName': 'Job-3', 'severe': 0, 'iterations': 1,
    'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['Job-3']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 7, 'jobName': 'Job-3'})
mdb.jobs['Job-3']._Message(STATUS, {'totalTime': 0.10890625, 'attempts': 1,
    'timeIncrement': 0.03796875, 'increment': 7, 'stepTime': 0.10890625,
    'step': 1, 'jobName': 'Job-3', 'severe': 0, 'iterations': 1,
    'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['Job-3']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 8, 'jobName': 'Job-3'})
mdb.jobs['Job-3']._Message(STATUS, {'totalTime': 0.165859375, 'attempts': 1,
    'timeIncrement': 0.056953125, 'increment': 8, 'stepTime': 0.165859375,
    'step': 1, 'jobName': 'Job-3', 'severe': 0, 'iterations': 1,
    'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['Job-3']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 9, 'jobName': 'Job-3'})
mdb.jobs['Job-3']._Message(STATUS, {'totalTime': 0.2512890625, 'attempts': 1,
    'timeIncrement': 0.0854296875, 'increment': 9, 'stepTime': 0.2512890625,
    'step': 1, 'jobName': 'Job-3', 'severe': 0, 'iterations': 1,
    'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['Job-3']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 10, 'jobName': 'Job-3'})
mdb.jobs['Job-3']._Message(STATUS, {'totalTime': 0.3512890625, 'attempts': 1,
    'timeIncrement': 0.1, 'increment': 10, 'stepTime': 0.3512890625, 'step': 1,
    'jobName': 'Job-3', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE,
    'equilibrium': 1})
mdb.jobs['Job-3']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 11, 'jobName': 'Job-3'})
mdb.jobs['Job-3']._Message(STATUS, {'totalTime': 0.4512890625, 'attempts': 1,
    'timeIncrement': 0.1, 'increment': 11, 'stepTime': 0.4512890625, 'step': 1,
    'jobName': 'Job-3', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE,
    'equilibrium': 1})
mdb.jobs['Job-3']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 12, 'jobName': 'Job-3'})
mdb.jobs['Job-3']._Message(STATUS, {'totalTime': 0.5512890625, 'attempts': 1,
    'timeIncrement': 0.1, 'increment': 12, 'stepTime': 0.5512890625, 'step': 1,
    'jobName': 'Job-3', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE,
    'equilibrium': 1})
mdb.jobs['Job-3']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 13, 'jobName': 'Job-3'})
mdb.jobs['Job-3']._Message(STATUS, {'totalTime': 0.6512890625, 'attempts': 1,
    'timeIncrement': 0.1, 'increment': 13, 'stepTime': 0.6512890625, 'step': 1,
    'jobName': 'Job-3', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE,
    'equilibrium': 1})
mdb.jobs['Job-3']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 14, 'jobName': 'Job-3'})
mdb.jobs['Job-3']._Message(STATUS, {'totalTime': 0.7512890625, 'attempts': 1,
    'timeIncrement': 0.1, 'increment': 14, 'stepTime': 0.7512890625, 'step': 1,
    'jobName': 'Job-3', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE,
    'equilibrium': 1})
mdb.jobs['Job-3']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 15, 'jobName': 'Job-3'})
mdb.jobs['Job-3']._Message(STATUS, {'totalTime': 0.8512890625, 'attempts': 1,
    'timeIncrement': 0.1, 'increment': 15, 'stepTime': 0.8512890625, 'step': 1,
    'jobName': 'Job-3', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE,
    'equilibrium': 1})
mdb.jobs['Job-3']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 16, 'jobName': 'Job-3'})
mdb.jobs['Job-3']._Message(STATUS, {'totalTime': 0.9512890625, 'attempts': 1,
    'timeIncrement': 0.1, 'increment': 16, 'stepTime': 0.9512890625, 'step': 1,
    'jobName': 'Job-3', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE,
    'equilibrium': 1})
mdb.jobs['Job-3']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 17, 'jobName': 'Job-3'})
mdb.jobs['Job-3']._Message(STATUS, {'totalTime': 1.0, 'attempts': 1,
    'timeIncrement': 0.0487109375000001, 'increment': 17, 'stepTime': 1.0,
    'step': 1, 'jobName': 'Job-3', 'severe': 0, 'iterations': 1,
    'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['Job-3']._Message(END_STEP, {'phase': STANDARD_PHASE, 'stepId': 1,
    'jobName': 'Job-3'})
mdb.jobs['Job-3']._Message(COMPLETED, {'phase': STANDARD_PHASE,
    'message': 'Analysis phase complete', 'jobName': 'Job-3'})
mdb.jobs['Job-3']._Message(JOB_COMPLETED, {'time': 'Mon May  2 15:08:37 2022',
    'jobName': 'Job-3'})
# Save by jiaor on 2022_05_02-15.13.11; build 2021 2020_03_06-22.50.37 167380
# Save by jiaor on 2022_05_02-16.47.22; build 2021 2020_03_06-22.50.37 167380
# Save by jiaor on 2022_05_02-16.47.24; build 2021 2020_03_06-22.50.37 167380
