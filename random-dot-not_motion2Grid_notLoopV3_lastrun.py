#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on 八月 13, 2022, at 10:58
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'random-dot-motion'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001', 'runID': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='D:\\Documents\\GitHub\\MEG-Raven\\random-dot-not_motion2Grid_notLoopV3_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1024, 768], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='deg')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "start"
startClock = core.Clock()
key_resp_3 = keyboard.Keyboard()
start_image = visual.ImageStim(
    win=win,
    name='start_image', units='deg', 
    image='start.png', mask=None,
    ori=0.0, pos=(0, 0), size=(30,20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
from psychopy import parallel
port = parallel.ParallelPort(address="0xD020")
port.setData(0)
startMark = 1
endMark = 8
stimMark = 2
respMark = 4
currentLoopNumber=-1
current_path = os.getcwd()  #获取当前路径
print(current_path)
path = current_path+'\\'+expInfo['participant']+'run.txt' #在当前路径创建名为test的文本文件
if os.path.exists(path):
    run_file=open(path, 'r+')
    
    run_lst = [int(i) for i in list(run_file.readline())[:-1]]
    idx_final=[]
    for i in range(10):
       idx_final.append([int(j) for j in run_file.readline().split(',')])
    idx_final=np.array(idx_final)
    while True:
        line = run_file.readline()
        if line == '':
            break
        run_num_orig = int(line)
    run_num=run_num_orig
    print(run_num_orig)
        
else:
    
    #初次运行，随机出题序
    run_num=0
    run_num_orig=0
    run_file = open(path,'w')
    run_lst=np.arange(1,11)
    np.random.shuffle(run_lst)
    run_file.writelines(''.join(str(i) for i in run_lst)+'\n')
    lst1=[]
    lst2=[]
    for i in range(18):
        if i%2==0:
            lst1.append(i)
        elif i%2==1:
            lst2.append(i)

    idx_lst=np.vstack([lst1,lst2])
    ## print(idx_lst)
    run0=idx_lst.copy()
    idx_seq = [run0]*10
    # print(idx_seq)
    idx_final=[]
    for run_seq in idx_seq:
    #    # time.sleep(0.1)
        for i in run_seq[:,0:run_seq.shape[1]-1]:
    #        x=1
            np.random.shuffle(i)
        np.random.shuffle(run_seq)
        for i in range(1,run_seq.shape[0]-1):
            # print('?', run_seq[i, :][-1] // 5,run_seq[i+1,:][0]//5)
            while (run_seq[i,:][-1]//2)==(run_seq[i+1,:][0]//2) or (run_seq[i,:][0]//2)==(run_seq[i-1,:][-1]//2) \
                    or (max(run_seq[i,:][-1],run_seq[i+1,:][0])<=4) or \
                    (max(run_seq[i,:][0],run_seq[i-1,:][-1])<=4):
                    # print('?')
                    np.random.shuffle(run_seq[i, :])
                    for j in range(len(run_seq[i,:])-1):
    #                    print(j,i)
                        if max(run_seq[i,j],run_seq[i,j+1])<=4:
    #                        print('**********************************************')
                            np.random.shuffle(run_seq[i, :])
                            break
                            # np.random.shuffle(run_seq[i,:])

                        # break
        # print('bef',run_seq)
        run_seq=np.array(run_seq)
        new_run=run_seq.reshape(1,-1)
        run_file.writelines(','.join(str(i) for i in new_run[0,:])+'\n')
        idx_final.append(new_run[0,:])
        # print('aft',new_run)
    idx_final=np.array(idx_final)
    # run_file.writelines(','.join(str(i) for i in idx_final)+'\n')
    run_file.writelines(str(run_num)+'\n')
answer_lst=np.concatenate([np.zeros(9),np.ones(9)],axis=0)
np.random.shuffle(answer_lst)

# Initialize components for Routine "rest"
restClock = core.Clock()
fixation_1 = visual.ShapeStim(
    win=win, name='fixation_1',units='deg', 
    size=(0.23, 0.23), vertices='circle',
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='crimson', fillColor='crimson',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "trial"
trialClock = core.Clock()
problem0 = visual.ImageStim(
    win=win,
    name='problem0', units='deg', 
    image='run1/figure0_0.jpg', mask=None,
    ori=0.0, pos=(-4.5,0), size=(4, 4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
problem1 = visual.ImageStim(
    win=win,
    name='problem1', units='deg', 
    image='run1/figure0_1.jpg', mask=None,
    ori=0.0, pos=(0,0), size=(4, 4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
problem2 = visual.ImageStim(
    win=win,
    name='problem2', units='deg', 
    image='run1/figure0_2.jpg', mask=None,
    ori=0.0, pos=(4.5,0), size=(4, 4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
problem3 = visual.ImageStim(
    win=win,
    name='problem3', units='deg', 
    image='run1/figure0_3.jpg', mask=None,
    ori=0.0, pos=(-4.5, 0), size=(4, 4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
problem4 = visual.ImageStim(
    win=win,
    name='problem4', units='deg', 
    image='run1/figure0_4.jpg', mask=None,
    ori=0.0, pos=(0, 0), size=(4, 4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
problem5 = visual.ImageStim(
    win=win,
    name='problem5', units='deg', 
    image='run1/figure0_6.jpg', mask=None,
    ori=0.0, pos=(4.5, 0), size=(4,4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
problem6 = visual.ImageStim(
    win=win,
    name='problem6', units='deg', 
    image='run1/figure0_6.jpg', mask=None,
    ori=0.0, pos=(-4.5, 0), size=(4, 4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
problem7 = visual.ImageStim(
    win=win,
    name='problem7', units='deg', 
    image='run1/figure0_7.jpg', mask=None,
    ori=0.0, pos=(0, 0), size=(4, 4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
answer = visual.ImageStim(
    win=win,
    name='answer', units='deg', 
    image='figure8.jpg', mask=None,
    ori=0.0, pos=(4.5, 0), size=(4, 4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
answer1 = visual.ImageStim(
    win=win,
    name='answer1', units='deg', 
    image='run1/target0_0.jpg', mask=None,
    ori=0.0, pos=(-2.5, 0), size=(4, 4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-10.0)
answer2 = visual.ImageStim(
    win=win,
    name='answer2', units='deg', 
    image='run1/target0_0.jpg', mask=None,
    ori=0.0, pos=(2.5, 0), size=(4, 4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-11.0)
key_resp = keyboard.Keyboard()
fixation1 = visual.ShapeStim(
    win=win, name='fixation1',units='deg', 
    size=(0.23, 0.23), vertices='circle',
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='burlywood', fillColor='burlywood',
    opacity=None, depth=-13.0, interpolate=True)
fixation2 = visual.ShapeStim(
    win=win, name='fixation2',units='deg', 
    size=(0.23, 0.23), vertices='circle',
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='burlywood', fillColor='burlywood',
    opacity=None, depth=-14.0, interpolate=True)
fixation3 = visual.ShapeStim(
    win=win, name='fixation3',units='deg', 
    size=(0.23, 0.23), vertices='circle',
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='burlywood', fillColor='burlywood',
    opacity=None, depth=-15.0, interpolate=True)
fixation4 = visual.ShapeStim(
    win=win, name='fixation4',units='deg', 
    size=(0.23, 0.23), vertices='circle',
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='burlywood', fillColor='burlywood',
    opacity=None, depth=-16.0, interpolate=True)

# Initialize components for Routine "middle_rest"
middle_restClock = core.Clock()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "start"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
if int(expInfo['runID'])==1:
    start_image.setImage('begin.png')
else:
    start_image.setImage('rest.png')
# keep track of which components have finished
startComponents = [key_resp_3, start_image]
for thisComponent in startComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
startClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "start"-------
while continueRoutine:
    # get current time
    t = startClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=startClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['s'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *start_image* updates
    if start_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start_image.frameNStart = frameN  # exact frame index
        start_image.tStart = t  # local t and not account for scr refresh
        start_image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_image, 'tStartRefresh')  # time at next scr refresh
        start_image.setAutoDraw(True)
    #if start_mark.status == STARTED:
    #    print("yes")
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in startComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "start"-------
for thisComponent in startComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.addData('key_resp_3.started', key_resp_3.tStartRefresh)
thisExp.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('start_image.started', start_image.tStartRefresh)
thisExp.addData('start_image.stopped', start_image.tStopRefresh)
port.setData(startMark)
core.wait(0.05)
port.setData(0)
# the Routine "start" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=18.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "rest"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    restComponents = [fixation_1]
    for thisComponent in restComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    restClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "rest"-------
    while continueRoutine:
        # get current time
        t = restClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=restClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation_1* updates
        if fixation_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_1.frameNStart = frameN  # exact frame index
            fixation_1.tStart = t  # local t and not account for scr refresh
            fixation_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_1, 'tStartRefresh')  # time at next scr refresh
            fixation_1.setAutoDraw(True)
        if fixation_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_1.tStartRefresh + 1.75+randint (-1,2)*0.25-frameTolerance:
                # keep track of stop time/frame for later
                fixation_1.tStop = t  # not accounting for scr refresh
                fixation_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation_1, 'tStopRefresh')  # time at next scr refresh
                fixation_1.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in restComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "rest"-------
    for thisComponent in restComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('fixation_1.started', fixation_1.tStartRefresh)
    trials.addData('fixation_1.stopped', fixation_1.tStopRefresh)
    # the Routine "rest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    currentLoopNumber += 1
    #print('num:',run_num)
    #print('lst:',run_lst[run_num])
    #print(str(run_lst[run_num])+'\\figure'+str(idx_final[run_num,currentLoopNumber]))
    problem0.setImage('run'+str(run_lst[run_num])+'\\figure'+str(idx_final[run_num,currentLoopNumber])+'_0.jpg')
    problem1.setImage('run'+str(run_lst[run_num])+'\\figure'+str(idx_final[run_num,currentLoopNumber])+'_1.jpg')
    problem2.setImage('run'+str(run_lst[run_num])+'\\figure'+str(idx_final[run_num,currentLoopNumber])+'_2.jpg')
    problem3.setImage('run'+str(run_lst[run_num])+'\\figure'+str(idx_final[run_num,currentLoopNumber])+'_3.jpg')
    problem4.setImage('run'+str(run_lst[run_num])+'\\figure'+str(idx_final[run_num,currentLoopNumber])+'_4.jpg')
    problem5.setImage('run'+str(run_lst[run_num])+'\\figure'+str(idx_final[run_num,currentLoopNumber])+'_5.jpg')
    problem6.setImage('run'+str(run_lst[run_num])+'\\figure'+str(idx_final[run_num,currentLoopNumber])+'_6.jpg')
    problem7.setImage('run'+str(run_lst[run_num])+'\\figure'+str(idx_final[run_num,currentLoopNumber])+'_7.jpg')
    rand_t1 = randint(-1,2)*0.25
    rand_t2 = randint(-1,2)*0.25
    rand_idx = int(answer_lst[currentLoopNumber])
    #rand_t2 = 0
    
    answer1.setImage('run'+str(run_lst[run_num])+'/target'+str(idx_final[run_num,currentLoopNumber])+'_'+str(rand_idx)+'.jpg')
    answer2.setImage('run'+str(run_lst[run_num])+'/target'+str(idx_final[run_num,currentLoopNumber])+'_'+str(1-rand_idx)+'.jpg')
    if rand_idx==0:
        corrAns='left'
    else:
        corrAns = 'right'
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    trialComponents = [problem0, problem1, problem2, problem3, problem4, problem5, problem6, problem7, answer, answer1, answer2, key_resp, fixation1, fixation2, fixation3, fixation4]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *problem0* updates
        if problem0.status == NOT_STARTED and tThisFlip >= 0.45-frameTolerance:
            # keep track of start time/frame for later
            problem0.frameNStart = frameN  # exact frame index
            problem0.tStart = t  # local t and not account for scr refresh
            problem0.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(problem0, 'tStartRefresh')  # time at next scr refresh
            problem0.setAutoDraw(True)
        if problem0.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > problem0.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                problem0.tStop = t  # not accounting for scr refresh
                problem0.frameNStop = frameN  # exact frame index
                win.timeOnFlip(problem0, 'tStopRefresh')  # time at next scr refresh
                problem0.setAutoDraw(False)
        
        # *problem1* updates
        if problem1.status == NOT_STARTED and tThisFlip >= 0.45-frameTolerance:
            # keep track of start time/frame for later
            problem1.frameNStart = frameN  # exact frame index
            problem1.tStart = t  # local t and not account for scr refresh
            problem1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(problem1, 'tStartRefresh')  # time at next scr refresh
            problem1.setAutoDraw(True)
        if problem1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > problem1.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                problem1.tStop = t  # not accounting for scr refresh
                problem1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(problem1, 'tStopRefresh')  # time at next scr refresh
                problem1.setAutoDraw(False)
        
        # *problem2* updates
        if problem2.status == NOT_STARTED and tThisFlip >= 0.45-frameTolerance:
            # keep track of start time/frame for later
            problem2.frameNStart = frameN  # exact frame index
            problem2.tStart = t  # local t and not account for scr refresh
            problem2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(problem2, 'tStartRefresh')  # time at next scr refresh
            problem2.setAutoDraw(True)
        if problem2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > problem2.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                problem2.tStop = t  # not accounting for scr refresh
                problem2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(problem2, 'tStopRefresh')  # time at next scr refresh
                problem2.setAutoDraw(False)
        
        # *problem3* updates
        if problem3.status == NOT_STARTED and tThisFlip >= 5.40+rand_t1-frameTolerance:
            # keep track of start time/frame for later
            problem3.frameNStart = frameN  # exact frame index
            problem3.tStart = t  # local t and not account for scr refresh
            problem3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(problem3, 'tStartRefresh')  # time at next scr refresh
            problem3.setAutoDraw(True)
        if problem3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > problem3.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                problem3.tStop = t  # not accounting for scr refresh
                problem3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(problem3, 'tStopRefresh')  # time at next scr refresh
                problem3.setAutoDraw(False)
        
        # *problem4* updates
        if problem4.status == NOT_STARTED and tThisFlip >= 5.40+rand_t1-frameTolerance:
            # keep track of start time/frame for later
            problem4.frameNStart = frameN  # exact frame index
            problem4.tStart = t  # local t and not account for scr refresh
            problem4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(problem4, 'tStartRefresh')  # time at next scr refresh
            problem4.setAutoDraw(True)
        if problem4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > problem4.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                problem4.tStop = t  # not accounting for scr refresh
                problem4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(problem4, 'tStopRefresh')  # time at next scr refresh
                problem4.setAutoDraw(False)
        
        # *problem5* updates
        if problem5.status == NOT_STARTED and tThisFlip >= 5.40+rand_t1-frameTolerance:
            # keep track of start time/frame for later
            problem5.frameNStart = frameN  # exact frame index
            problem5.tStart = t  # local t and not account for scr refresh
            problem5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(problem5, 'tStartRefresh')  # time at next scr refresh
            problem5.setAutoDraw(True)
        if problem5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > problem5.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                problem5.tStop = t  # not accounting for scr refresh
                problem5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(problem5, 'tStopRefresh')  # time at next scr refresh
                problem5.setAutoDraw(False)
        
        # *problem6* updates
        if problem6.status == NOT_STARTED and tThisFlip >= 10.35+rand_t1+rand_t2-frameTolerance:
            # keep track of start time/frame for later
            problem6.frameNStart = frameN  # exact frame index
            problem6.tStart = t  # local t and not account for scr refresh
            problem6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(problem6, 'tStartRefresh')  # time at next scr refresh
            problem6.setAutoDraw(True)
        if problem6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > problem6.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                problem6.tStop = t  # not accounting for scr refresh
                problem6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(problem6, 'tStopRefresh')  # time at next scr refresh
                problem6.setAutoDraw(False)
        
        # *problem7* updates
        if problem7.status == NOT_STARTED and tThisFlip >= 10.35+rand_t1+rand_t2-frameTolerance:
            # keep track of start time/frame for later
            problem7.frameNStart = frameN  # exact frame index
            problem7.tStart = t  # local t and not account for scr refresh
            problem7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(problem7, 'tStartRefresh')  # time at next scr refresh
            problem7.setAutoDraw(True)
        if problem7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > problem7.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                problem7.tStop = t  # not accounting for scr refresh
                problem7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(problem7, 'tStopRefresh')  # time at next scr refresh
                problem7.setAutoDraw(False)
        
        # *answer* updates
        if answer.status == NOT_STARTED and tThisFlip >= 10.35+rand_t1+rand_t2-frameTolerance:
            # keep track of start time/frame for later
            answer.frameNStart = frameN  # exact frame index
            answer.tStart = t  # local t and not account for scr refresh
            answer.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(answer, 'tStartRefresh')  # time at next scr refresh
            answer.setAutoDraw(True)
        if answer.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > answer.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                answer.tStop = t  # not accounting for scr refresh
                answer.frameNStop = frameN  # exact frame index
                win.timeOnFlip(answer, 'tStopRefresh')  # time at next scr refresh
                answer.setAutoDraw(False)
        if problem0.status == STARTED:
            port.setData(stimMark)
            core.wait(0.05)
            port.setData(0)
            
        if problem3.status == STARTED:
            port.setData(stimMark)
            core.wait(0.05)
            port.setData(0)
            
        if problem6.status == STARTED:
            port.setData(stimMark)
            core.wait(0.05)
            port.setData(0)
            
        if answer1.status == STARTED:
            port.setData(stimMark)
            core.wait(0.05)
            port.setData(0)
            
        if len(_key_resp_allKeys):
            port.setData(respMark)
            core.wait(0.05)
            port.setData(0)
        
        # *answer1* updates
        if answer1.status == NOT_STARTED and tThisFlip >= 15.3+rand_t1+rand_t2-frameTolerance:
            # keep track of start time/frame for later
            answer1.frameNStart = frameN  # exact frame index
            answer1.tStart = t  # local t and not account for scr refresh
            answer1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(answer1, 'tStartRefresh')  # time at next scr refresh
            answer1.setAutoDraw(True)
        if answer1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > answer1.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                answer1.tStop = t  # not accounting for scr refresh
                answer1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(answer1, 'tStopRefresh')  # time at next scr refresh
                answer1.setAutoDraw(False)
        
        # *answer2* updates
        if answer2.status == NOT_STARTED and tThisFlip >= 15.3+rand_t1+rand_t2-frameTolerance:
            # keep track of start time/frame for later
            answer2.frameNStart = frameN  # exact frame index
            answer2.tStart = t  # local t and not account for scr refresh
            answer2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(answer2, 'tStartRefresh')  # time at next scr refresh
            answer2.setAutoDraw(True)
        if answer2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > answer2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                answer2.tStop = t  # not accounting for scr refresh
                answer2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(answer2, 'tStopRefresh')  # time at next scr refresh
                answer2.setAutoDraw(False)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 15.3+rand_t1+rand_t2-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                key_resp.tStop = t  # not accounting for scr refresh
                key_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
                key_resp.status = FINISHED
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['left', 'right'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # was this correct?
                if (key_resp.keys == str(corrAns)) or (key_resp.keys == corrAns):
                    key_resp.corr = 1
                else:
                    key_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *fixation1* updates
        if fixation1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation1.frameNStart = frameN  # exact frame index
            fixation1.tStart = t  # local t and not account for scr refresh
            fixation1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation1, 'tStartRefresh')  # time at next scr refresh
            fixation1.setAutoDraw(True)
        if fixation1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation1.tStartRefresh + 3.45-frameTolerance:
                # keep track of stop time/frame for later
                fixation1.tStop = t  # not accounting for scr refresh
                fixation1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation1, 'tStopRefresh')  # time at next scr refresh
                fixation1.setAutoDraw(False)
        
        # *fixation2* updates
        if fixation2.status == NOT_STARTED and tThisFlip >= 3.45-frameTolerance:
            # keep track of start time/frame for later
            fixation2.frameNStart = frameN  # exact frame index
            fixation2.tStart = t  # local t and not account for scr refresh
            fixation2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation2, 'tStartRefresh')  # time at next scr refresh
            fixation2.setAutoDraw(True)
        if fixation2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation2.tStartRefresh + 4.95+rand_t1-frameTolerance:
                # keep track of stop time/frame for later
                fixation2.tStop = t  # not accounting for scr refresh
                fixation2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation2, 'tStopRefresh')  # time at next scr refresh
                fixation2.setAutoDraw(False)
        
        # *fixation3* updates
        if fixation3.status == NOT_STARTED and tThisFlip >= 8.4+rand_t1-frameTolerance:
            # keep track of start time/frame for later
            fixation3.frameNStart = frameN  # exact frame index
            fixation3.tStart = t  # local t and not account for scr refresh
            fixation3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation3, 'tStartRefresh')  # time at next scr refresh
            fixation3.setAutoDraw(True)
        if fixation3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation3.tStartRefresh + 4.95+rand_t2-frameTolerance:
                # keep track of stop time/frame for later
                fixation3.tStop = t  # not accounting for scr refresh
                fixation3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation3, 'tStopRefresh')  # time at next scr refresh
                fixation3.setAutoDraw(False)
        
        # *fixation4* updates
        if fixation4.status == NOT_STARTED and tThisFlip >= 13.35+rand_t1+rand_t2-frameTolerance:
            # keep track of start time/frame for later
            fixation4.frameNStart = frameN  # exact frame index
            fixation4.tStart = t  # local t and not account for scr refresh
            fixation4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation4, 'tStartRefresh')  # time at next scr refresh
            fixation4.setAutoDraw(True)
        if fixation4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation4.tStartRefresh + 3.95-frameTolerance:
                # keep track of stop time/frame for later
                fixation4.tStop = t  # not accounting for scr refresh
                fixation4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation4, 'tStopRefresh')  # time at next scr refresh
                fixation4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('problem0.started', problem0.tStartRefresh)
    trials.addData('problem0.stopped', problem0.tStopRefresh)
    trials.addData('problem1.started', problem1.tStartRefresh)
    trials.addData('problem1.stopped', problem1.tStopRefresh)
    trials.addData('problem2.started', problem2.tStartRefresh)
    trials.addData('problem2.stopped', problem2.tStopRefresh)
    trials.addData('problem3.started', problem3.tStartRefresh)
    trials.addData('problem3.stopped', problem3.tStopRefresh)
    trials.addData('problem4.started', problem4.tStartRefresh)
    trials.addData('problem4.stopped', problem4.tStopRefresh)
    trials.addData('problem5.started', problem5.tStartRefresh)
    trials.addData('problem5.stopped', problem5.tStopRefresh)
    trials.addData('problem6.started', problem6.tStartRefresh)
    trials.addData('problem6.stopped', problem6.tStopRefresh)
    trials.addData('problem7.started', problem7.tStartRefresh)
    trials.addData('problem7.stopped', problem7.tStopRefresh)
    trials.addData('answer.started', answer.tStartRefresh)
    trials.addData('answer.stopped', answer.tStopRefresh)
    trials.addData('answer1.started', answer1.tStartRefresh)
    trials.addData('answer1.stopped', answer1.tStopRefresh)
    trials.addData('answer2.started', answer2.tStartRefresh)
    trials.addData('answer2.stopped', answer2.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           key_resp.corr = 1;  # correct non-response
        else:
           key_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('key_resp.keys',key_resp.keys)
    trials.addData('key_resp.corr', key_resp.corr)
    if key_resp.keys != None:  # we had a response
        trials.addData('key_resp.rt', key_resp.rt)
    trials.addData('key_resp.started', key_resp.tStartRefresh)
    trials.addData('key_resp.stopped', key_resp.tStopRefresh)
    trials.addData('fixation1.started', fixation1.tStartRefresh)
    trials.addData('fixation1.stopped', fixation1.tStopRefresh)
    trials.addData('fixation2.started', fixation2.tStartRefresh)
    trials.addData('fixation2.stopped', fixation2.tStopRefresh)
    trials.addData('fixation3.started', fixation3.tStartRefresh)
    trials.addData('fixation3.stopped', fixation3.tStopRefresh)
    trials.addData('fixation4.started', fixation4.tStartRefresh)
    trials.addData('fixation4.stopped', fixation4.tStopRefresh)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 18.0 repeats of 'trials'


# ------Prepare to start Routine "middle_rest"-------
continueRoutine = True
# update component parameters for each repeat
if problem0.status == STARTED:
    port.setData(endMark)
    core.wait(0.05)
    port.setData(0)
  
# keep track of which components have finished
middle_restComponents = []
for thisComponent in middle_restComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
middle_restClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "middle_rest"-------
while continueRoutine:
    # get current time
    t = middle_restClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=middle_restClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in middle_restComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "middle_rest"-------
for thisComponent in middle_restComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "middle_rest" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
