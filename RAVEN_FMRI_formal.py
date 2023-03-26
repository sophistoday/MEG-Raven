#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on 十一月 19, 2022, at 14:17
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
from psychopy import monitors

myMon = monitors.Monitor("testMonitor",distance=110,width=30)
myMon.setSizePix((1024, 768))

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
filename = _thisDir + os.sep + u'data/%s_Run%s_%s_%s' % (expInfo['participant'],expInfo['runID'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='RAVEN_FMRI_formal.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

#stimulus size
pixelPerMilimeterHor = 1024/390
pixelPerMilimeterVer = 768/295

imgAngle=4
imgPixelHor = int(pixelPerMilimeterHor * (2 * 1100 * tan(imgAngle/180*pi/2)))
imgPixelVer = int(pixelPerMilimeterVer * (2 * 1100 * tan(imgAngle/180*pi/2)))

fixAngle=0.2

guide_picHorDeg = 10
guide_picVerDeg = 7.5
# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1024, 768], fullscr=False, screen=1,
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor=myMon, color=[-1.0,-1.0,-1.0], colorSpace='rgb',
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
#set totalCorrNum
totalCorrNum=0

# Initialize components for Routine "start"
startClock = core.Clock()
key_resp_3 = keyboard.Keyboard()
start_image = visual.ImageStim(
    win=win,
    name='start_image', units='deg', 
    image='begin.png', mask=None,
    ori=0.0, pos=(0, 0), size=(guide_picHorDeg,guide_picVerDeg),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
#from psychopy import parallel
#port = parallel.ParallelPort(address="0xD020")
#port.setData(0)
#startMark = 1
#endMark = 8
#stimMark = 2
#respMark = 4
every_run_num = 27
currentLoopNumber=-1
totalRunTime = 8
current_path = os.getcwd()  # 获取当前路径
#print(current_path)
path = current_path + '/' + expInfo['participant'] + 'run.txt'  # 在当前路径创建名为run的文本文件
if os.path.exists(path):
    run_file = open(path, 'r+')
    run_num = int(expInfo['runID']) - 1
    run_lst = [int(i) for i in list(run_file.readline())[:-1]]
    idx_final = []
    for i in range(totalRunTime):
        idx_final.append([int(j) for j in run_file.readline().split(',')])
    idx_final = np.array(idx_final)
    time_lst = []
    for i in range(totalRunTime):
        time_lst.append([int(j) for j in run_file.readline().split(',')])
    time_lst = np.array(time_lst)
    time_lst = time_lst.reshape(totalRunTime, every_run_num, 2)
    while True:
        line = run_file.readline()
        if line == '':
            break
#        run_num_orig = int(line)
#    run_num=run_num_orig
#    print(run_num_orig)

else:
    # 初次运行，随机出题序
    run_num = 0
    
    run_file = open(path, 'w')
    run_lst = np.arange(1, totalRunTime+1) #生成runID的序列
    np.random.shuffle(run_lst)
    run_file.writelines(''.join(str(i) for i in run_lst) + '\n')
    lst1 = []
    lst2 = []
    lst3 = []
    for i in range(every_run_num):       #将每一个run的下标分成三组，每一组包含所有类
        if i % 3 == 0:
            lst1.append(i)
        elif i % 3 == 1:
            lst2.append(i)
        elif i%3==2:
            lst3.append(i)

    idx_lst = np.vstack([lst1, lst2,lst3])#每一个lst是一类中的一个
    ## print(idx_lst)
    run0 = idx_lst.copy()                 #一个run的下标
    idx_seq = [run0] * totalRunTime       #所有run的下标
    # print(idx_seq)
    idx_final = []
    for run_seq in idx_seq:              #遍历每一个run
        #    # time.sleep(0.1)
        for i in run_seq[:, 0:run_seq.shape[1] - 1]:#每一个组打乱
            #        x=1
            np.random.shuffle(i)
        np.random.shuffle(run_seq)#每一个组序打乱
        for i in range(1, run_seq.shape[0] - 1):
            # print('?', run_seq[i, :][-1] // 5,run_seq[i+1,:][0]//5)
            while (run_seq[i, :][-1] // 3) == (run_seq[i + 1, :][0] // 3) or (run_seq[i, :][0] // 3) == (  #判断组之间有没有相同类
                    run_seq[i - 1, :][-1] // 3) \
                    or (max(run_seq[i, :][-1], run_seq[i + 1, :][0]) <= 6) or \
                    (max(run_seq[i, :][0], run_seq[i - 1, :][-1]) <= 6):                                   #判断组之间有没有同样的const
                # print('?')
                np.random.shuffle(run_seq[i, :])
                for j in range(len(run_seq[i, :]) - 1):
                    #                    print(j,i)
                    if max(run_seq[i, j], run_seq[i, j + 1]) <= 6:
                        #                        print('**********************************************')
                        np.random.shuffle(run_seq[i, :])
                        break
                        # np.random.shuffle(run_seq[i,:])

                    # break
        # print('bef',run_seq)
        run_seq = np.array(run_seq)
        new_run = run_seq.reshape(1, -1)
        run_file.writelines(','.join(str(i) for i in new_run[0, :]) + '\n')
        idx_final.append(new_run[0, :])
        # print('aft',new_run)
    idx_final = np.array(idx_final)
    time_lst=[]
    for i in range(totalRunTime):
        # time_list.append(np.round(np.random.rand(1,every_run_num * 2),2))
        lst=np.hstack([np.arange(0,25),[1,2]])
        temp=np.hstack([lst,-lst])
        np.random.shuffle(temp)

        time_lst.append(temp)
    # print(np.mean(time_list[i]))
    time_lst=np.array(time_lst)
    for line in time_lst:
        # break
        run_file.writelines(','.join(str(i) for i in line) + '\n')
    time_lst = time_lst.reshape(totalRunTime, every_run_num, 2)
if (int(expInfo['runID'])-1)%2==0:
    answer_lst = np.concatenate([np.zeros(int(every_run_num/2)+1), np.ones(int(every_run_num/2))], axis=0)
else:
    answer_lst = np.concatenate([np.zeros(int(every_run_num/2)), np.ones(int(every_run_num/2)+1)], axis=0)
np.random.shuffle(answer_lst)

#print(imgPixelHor)
#arrPixelhor = int(pixelPerMilimeterHor * (2 * 1100 * tan(imgAngle/180*pi/2)));
mouse_2 = event.Mouse(win=win)
x, y = [None, None]
mouse_2.mouseClock = core.Clock()

# Initialize components for Routine "routine_1"
routine_1Clock = core.Clock()
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "end"
endClock = core.Clock()
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices='circle',units='deg', 
    size=(fixAngle, fixAngle),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "rest"
restClock = core.Clock()
fixation_1 = visual.ShapeStim(
    win=win, name='fixation_1',units='deg', 
    size=(fixAngle, fixAngle), vertices='circle',
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "trial"
trialClock = core.Clock()
problem0 = visual.ImageStim(
    win=win,
    name='problem0', units='pix', 
    image='run1/figure0_0.jpg', mask=None,
    ori=0.0, pos=(-imgPixelHor-30,0), size=(imgPixelHor,imgPixelVer),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
problem1 = visual.ImageStim(
    win=win,
    name='problem1', units='pix', 
    image='run1/figure0_1.jpg', mask=None,
    ori=0.0, pos=(0, 0), size=(imgPixelHor,imgPixelVer),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
problem2 = visual.ImageStim(
    win=win,
    name='problem2', units='pix', 
    image='run1/figure0_2.jpg', mask=None,
    ori=0.0, pos=(imgPixelHor+30, 0), size=(imgPixelHor,imgPixelVer),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
problem6 = visual.ImageStim(
    win=win,
    name='problem6', units='pix', 
    image='run1/figure0_3.jpg', mask=None,
    ori=0.0, pos=(-imgPixelHor-30,0), size=(imgPixelHor,imgPixelVer),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
problem7 = visual.ImageStim(
    win=win,
    name='problem7', units='pix', 
    image='run1/figure0_4.jpg', mask=None,
    ori=0.0, pos=(0, 0), size=(imgPixelHor,imgPixelVer),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
answer = visual.ImageStim(
    win=win,
    name='answer', units='pix', 
    image='figure8.jpg', mask=None,
    ori=0.0, pos=(imgPixelHor+30, 0), size=(imgPixelHor,imgPixelVer),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
answer1 = visual.ImageStim(
    win=win,
    name='answer1', units='pix', 
    image='run1/target0_0.jpg', mask=None,
    ori=0.0, pos=(-imgPixelHor-30,0), size=(imgPixelHor,imgPixelVer),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
answer2 = visual.ImageStim(
    win=win,
    name='answer2', units='pix', 
    image='run1/target0_0.jpg', mask=None,
    ori=0.0, pos=(imgPixelHor+30, 0), size=(imgPixelHor,imgPixelVer),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
key_resp = keyboard.Keyboard()
fixation2 = visual.ShapeStim(
    win=win, name='fixation2', vertices='circle',units='deg', 
    size=(fixAngle, fixAngle),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-10.0, interpolate=True)
fixation3 = visual.ShapeStim(
    win=win, name='fixation3', vertices='circle',units='deg', 
    size=(fixAngle, fixAngle),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-11.0, interpolate=True)
key_resp_4 = keyboard.Keyboard()
fixation = visual.ShapeStim(
    win=win, name='fixation', vertices='circle',units='deg', 
    size=(fixAngle, fixAngle),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-13.0, interpolate=True)
arrow = visual.ImageStim(
    win=win,
    name='arrow', units='pix', 
    image='newFixa.png', mask=None,
    ori=0.0, pos=(0, 0), size=(imgPixelHor,imgPixelVer),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-14.0)

# Initialize components for Routine "middle_rest"
middle_restClock = core.Clock()
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image=None, mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
polygon_2 = visual.ShapeStim(
    win=win, name='polygon_2', vertices='circle',units='deg', 
    size=(fixAngle, fixAngle),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)

# Initialize components for Routine "end"
endClock = core.Clock()
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices='circle',units='deg', 
    size=(fixAngle, fixAngle),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "start"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
#if int(expInfo['runID'])==1:
#    start_image.setImage('begin.png')
#else:
#    start_image.setImage('rest.png')
mouse_2.setVisible(False)
# setup some python lists for storing info about the mouse_2
gotValidClick = False  # until a click is received
# keep track of which components have finished
startComponents = [key_resp_3, start_image, mouse_2]
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
        theseKeys = key_resp_3.getKeys(keyList=['3', '4'], waitRelease=False)
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
    # *mouse_2* updates
    if mouse_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_2.frameNStart = frameN  # exact frame index
        mouse_2.tStart = t  # local t and not account for scr refresh
        mouse_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_2, 'tStartRefresh')  # time at next scr refresh
        mouse_2.status = STARTED
        mouse_2.mouseClock.reset()
        prevButtonState = mouse_2.getPressed()  # if button is down already this ISN'T a new click
    if mouse_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mouse_2.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            mouse_2.tStop = t  # not accounting for scr refresh
            mouse_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mouse_2, 'tStopRefresh')  # time at next scr refresh
            mouse_2.status = FINISHED
    if mouse_2.status == STARTED:  # only update if started and not finished!
        buttons = mouse_2.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # abort routine on response
                continueRoutine = False
    
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
# store data for thisExp (ExperimentHandler)
x, y = mouse_2.getPos()
buttons = mouse_2.getPressed()
thisExp.addData('mouse_2.x', x)
thisExp.addData('mouse_2.y', y)
thisExp.addData('mouse_2.leftButton', buttons[0])
thisExp.addData('mouse_2.midButton', buttons[1])
thisExp.addData('mouse_2.rightButton', buttons[2])
thisExp.addData('mouse_2.started', mouse_2.tStart)
thisExp.addData('mouse_2.stopped', mouse_2.tStop)
thisExp.nextEntry()
# the Routine "start" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "routine_1"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
routine_1Components = [key_resp_2]
for thisComponent in routine_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
routine_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "routine_1"-------
while continueRoutine:
    # get current time
    t = routine_1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routine_1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['s'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in routine_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "routine_1"-------
key_resp_2_stopTime=tThisFlipGlobal
for thisComponent in routine_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2_stopTime)
thisExp.nextEntry()
# the Routine "routine_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "end"-------
continueRoutine = True
routineTimer.add(10.000000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = [polygon]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
#polygon_start_time = 0   #补偿注视点开始时间
# -------Run Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *polygon* updates
    if polygon.status == NOT_STARTED and tThisFlip >= 0.0:
        # keep track of start time/frame for later
        #polygon_start_time  = tThisFlipGlobal
        polygon.frameNStart = frameN  # exact frame index
        polygon.tStart = t  # local t and not account for scr refresh
        polygon.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
        polygon.setAutoDraw(True)
    if polygon.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > polygon.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            polygon.tStop = t  # not accounting for scr refresh

            polygon.frameNStop = frameN  # exact frame index
            win.timeOnFlip(polygon, 'tStopRefresh')  # time at next scr refresh
            polygon.tStopRefresh = tThisFlipGlobal
            polygon.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
polygon_stopTime=tThisFlipGlobal
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('polygon.started', polygon.tStartRefresh)
thisExp.addData('polygon.stopped', polygon_stopTime)#polygon.tStopRefresh

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=27.0, method='sequential', 
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
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    compensate_clock = core.Clock()
    compensate_clock.reset
    
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
    fixation_1_startTime = 0
    # -------Run Routine "rest"-------
    while continueRoutine and routineTimer.getTime() > 0:
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
            fixation_1_startTime = tThisFlipGlobal
            fixation_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_1, 'tStartRefresh')  # time at next scr refresh
            fixation_1.setAutoDraw(True)
        if fixation_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_1.tStartRefresh + 1-frameTolerance:
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
    trials.addData('fixation_1.started', fixation_1_startTime )
    trials.addData('fixation_1.stopped', tThisFlipGlobal)
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    currentLoopNumber += 1
    #print('num:',run_num)
    #print('lst:',run_lst[run_num])
    #print(str(run_lst[run_num])+'\\figure'+str(idx_final[run_num,currentLoopNumber]))
    problem0.setImage('run'+str(run_lst[run_num])+'/figure'+str(idx_final[run_num,currentLoopNumber])+'_0.jpg')
    problem1.setImage('run'+str(run_lst[run_num])+'/figure'+str(idx_final[run_num,currentLoopNumber])+'_1.jpg')
    problem2.setImage('run'+str(run_lst[run_num])+'/figure'+str(idx_final[run_num,currentLoopNumber])+'_2.jpg')
    #problem3.setImage('run'+str(run_lst[run_num])+'\\figure'+str(idx_final[run_num,currentLoopNumber])+'_3.jpg')
    #problem4.setImage('run'+str(run_lst[run_num])+'\\figure'+str(idx_final[run_num,currentLoopNumber])+'_4.jpg')
    #problem5.setImage('run'+str(run_lst[run_num])+'_1\\figure'+str(idx_final[run_num,currentLoopNumber])+'_5.jpg')
    problem6.setImage('run'+str(run_lst[run_num])+'/figure'+str(idx_final[run_num,currentLoopNumber])+'_3.jpg')
    problem7.setImage('run'+str(run_lst[run_num])+'/figure'+str(idx_final[run_num,currentLoopNumber])+'_4.jpg')
    rand_t1 = int(time_lst[run_num,currentLoopNumber,0])*0.01
    rand_t2 = int(time_lst[run_num,currentLoopNumber,1])*0.01
    rand_idx = int(answer_lst[currentLoopNumber])
    #rand_t2 = 0
    
    answer1.setImage('run'+str(run_lst[run_num])+'/target'+str(idx_final[run_num,currentLoopNumber])+'_'+str(rand_idx)+'.jpg')
    answer2.setImage('run'+str(run_lst[run_num])+'/target'+str(idx_final[run_num,currentLoopNumber])+'_'+str(1-rand_idx)+'.jpg')
    #answer3.setImage('run'+str(run_lst[run_num])+'\\figure'+str(idx_final[run_num,currentLoopNumber])+'_6.jpg')
    if rand_idx==0:
        corrAns1='1'
        corrAns2='2'
    else:
        corrAns1='3'
        corrAns2='4'
    #if rand_idx==0:
    #    corrAns1='left'
    #    
    #else:
    #    corrAns1='right'
    
    #fixOuterSize = int(pixelPerMilimeterHor * (2 * 1000 * tan(fixOuterAngle/180*pi/2)));
    #fixInnerSize = int(pixelPerMilimeterHor * (2 * 1000 * tan(fixInnerAngle/180*pi/2)));
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    key_resp_4.keys = []
    key_resp_4.rt = []
    _key_resp_4_allKeys = []
    # keep track of which components have finished
    trialComponents = [problem0, problem1, problem2, problem6, problem7, answer, answer1, answer2, key_resp, fixation2, fixation3, key_resp_4, fixation, arrow]
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
        if problem0.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            problem0.frameNStart = frameN  # exact frame index
            problem0.tStart = t  # local t and not account for scr refresh
            problem0.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(problem0, 'tStartRefresh')  # time at next scr refresh
            problem0.setAutoDraw(True)
        if problem0.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > problem0.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                problem0.tStop = t  # not accounting for scr refresh
                problem0.frameNStop = frameN  # exact frame index
                win.timeOnFlip(problem0, 'tStopRefresh')  # time at next scr refresh
                problem0.setAutoDraw(False)
        
        # *problem1* updates
        if problem1.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            problem1.frameNStart = frameN  # exact frame index
            problem1.tStart = t  # local t and not account for scr refresh
            problem1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(problem1, 'tStartRefresh')  # time at next scr refresh
            problem1.setAutoDraw(True)
        if problem1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > problem1.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                problem1.tStop = t  # not accounting for scr refresh
                problem1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(problem1, 'tStopRefresh')  # time at next scr refresh
                problem1.setAutoDraw(False)
        
        # *problem2* updates
        if problem2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            problem2.frameNStart = frameN  # exact frame index
            problem2.tStart = t  # local t and not account for scr refresh
            problem2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(problem2, 'tStartRefresh')  # time at next scr refresh
            problem2.setAutoDraw(True)
        if problem2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > problem2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                problem2.tStop = t  # not accounting for scr refresh
                problem2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(problem2, 'tStopRefresh')  # time at next scr refresh
                problem2.setAutoDraw(False)
        
        # *problem6* updates
        if problem6.status == NOT_STARTED and tThisFlip >= 3.5+rand_t1-frameTolerance:
            # keep track of start time/frame for later
            problem6.frameNStart = frameN  # exact frame index
            problem6.tStart = t  # local t and not account for scr refresh
            problem6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(problem6, 'tStartRefresh')  # time at next scr refresh
            problem6.setAutoDraw(True)
        if problem6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > problem6.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                problem6.tStop = t  # not accounting for scr refresh
                problem6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(problem6, 'tStopRefresh')  # time at next scr refresh
                problem6.setAutoDraw(False)
        
        # *problem7* updates
        if problem7.status == NOT_STARTED and tThisFlip >= 3.5+rand_t1-frameTolerance:
            # keep track of start time/frame for later
            problem7.frameNStart = frameN  # exact frame index
            problem7.tStart = t  # local t and not account for scr refresh
            problem7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(problem7, 'tStartRefresh')  # time at next scr refresh
            problem7.setAutoDraw(True)
        if problem7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > problem7.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                problem7.tStop = t  # not accounting for scr refresh
                problem7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(problem7, 'tStopRefresh')  # time at next scr refresh
                problem7.setAutoDraw(False)
        
        # *answer* updates
        if answer.status == NOT_STARTED and tThisFlip >= 3.5+rand_t1-frameTolerance:
            # keep track of start time/frame for later
            answer.frameNStart = frameN  # exact frame index
            answer.tStart = t  # local t and not account for scr refresh
            answer.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(answer, 'tStartRefresh')  # time at next scr refresh
            answer.setAutoDraw(True)
        if answer.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > answer.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                answer.tStop = t  # not accounting for scr refresh
                answer.frameNStop = frameN  # exact frame index
                win.timeOnFlip(answer, 'tStopRefresh')  # time at next scr refresh
                answer.setAutoDraw(False)
        #if problem0.status == STARTED:
        #    port.setData(stimMark)
        #    core.wait(0.05)
        #    port.setData(0)
        #    
        #if problem3.status == STARTED:
        #    port.setData(stimMark)
        #    core.wait(0.05)
        #    port.setData(0)
        #    
        #if problem6.status == STARTED:
        #    port.setData(stimMark)
        #    core.wait(0.05)
        #    port.setData(0)
        #    
        #if answer1.status == STARTED:
        #    port.setData(stimMark)
        #    core.wait(0.05)
        #    port.setData(0)
        #    
        #if len(_key_resp_allKeys):
        #    port.setData(respMark)
        #    core.wait(0.05)
        #    port.setData(0)
        
        # *answer1* updates
        if answer1.status == NOT_STARTED and tThisFlip >= 6.5+rand_t1+rand_t2-frameTolerance:
            # keep track of start time/frame for later
            answer1.frameNStart = frameN  # exact frame index
            answer1.tStart = t  # local t and not account for scr refresh
            answer1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(answer1, 'tStartRefresh')  # time at next scr refresh
            answer1.setAutoDraw(True)
        if answer1.status == STARTED:
            if bool(key_resp.status == FINISHED):
                # keep track of stop time/frame for later
                answer1.tStop = t  # not accounting for scr refresh
                answer1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(answer1, 'tStopRefresh')  # time at next scr refresh
                answer1.setAutoDraw(False)
        
        # *answer2* updates
        if answer2.status == NOT_STARTED and tThisFlip >= 6.5+rand_t1+rand_t2-frameTolerance:
            # keep track of start time/frame for later
            answer2.frameNStart = frameN  # exact frame index
            answer2.tStart = t  # local t and not account for scr refresh
            answer2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(answer2, 'tStartRefresh')  # time at next scr refresh
            answer2.setAutoDraw(True)
        if answer2.status == STARTED:
            if bool(key_resp.status == FINISHED):
                # keep track of stop time/frame for later
                answer2.tStop = t  # not accounting for scr refresh
                answer2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(answer2, 'tStopRefresh')  # time at next scr refresh
                answer2.setAutoDraw(False)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 6.5+rand_t1+rand_t2-frameTolerance:
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
            theseKeys = key_resp.getKeys(keyList=['1', '3'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # was this correct?
                if (key_resp.keys == str(corrAns1)) or (key_resp.keys == corrAns1):
                    key_resp.corr = 1
                else:
                    key_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *fixation2* updates
        if fixation2.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
            # keep track of start time/frame for later
            fixation2.frameNStart = frameN  # exact frame index
            fixation2.tStart = t  # local t and not account for scr refresh
            fixation2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation2, 'tStartRefresh')  # time at next scr refresh
            fixation2.setAutoDraw(True)
        if fixation2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation2.tStartRefresh + 1+rand_t1-frameTolerance:
                # keep track of stop time/frame for later
                fixation2.tStop = t  # not accounting for scr refresh
                fixation2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation2, 'tStopRefresh')  # time at next scr refresh
                fixation2.setAutoDraw(False)
        
        # *fixation3* updates
        if fixation3.status == NOT_STARTED and tThisFlip >= 5.5+rand_t1-frameTolerance:
            # keep track of start time/frame for later
            fixation3.frameNStart = frameN  # exact frame index
            fixation3.tStart = t  # local t and not account for scr refresh
            fixation3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation3, 'tStartRefresh')  # time at next scr refresh
            fixation3.setAutoDraw(True)
        if fixation3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation3.tStartRefresh + 1+rand_t2-frameTolerance:
                # keep track of stop time/frame for later
                fixation3.tStop = t  # not accounting for scr refresh
                fixation3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation3, 'tStopRefresh')  # time at next scr refresh
                fixation3.setAutoDraw(False)
        
        # *key_resp_4* updates
        waitOnFlip = False
        if key_resp_4.status == NOT_STARTED and tThisFlip >= 6.5+rand_t1+rand_t2-frameTolerance:
            # keep track of start time/frame for later
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.tStart = t  # local t and not account for scr refresh
            key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_4.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_4.tStop = t  # not accounting for scr refresh
                key_resp_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_4, 'tStopRefresh')  # time at next scr refresh
                key_resp_4.status = FINISHED
        if key_resp_4.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_4.getKeys(keyList=['2', '4'], waitRelease=False)
            _key_resp_4_allKeys.extend(theseKeys)
            if len(_key_resp_4_allKeys):
                key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                # was this correct?
                if (key_resp_4.keys == str(corrAns2)) or (key_resp_4.keys == corrAns2):
                    key_resp_4.corr = 1
                else:
                    key_resp_4.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *fixation* updates
        if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation.frameNStart = frameN  # exact frame index
            fixation.tStart = t  # local t and not account for scr refresh
            fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
            fixation.setAutoDraw(True)
        if fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                fixation.tStop = t  # not accounting for scr refresh
                fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation, 'tStopRefresh')  # time at next scr refresh
                fixation.setAutoDraw(False)
        
        # *arrow* updates
        if arrow.status == NOT_STARTED and tThisFlip >= 6.5+rand_t1+rand_t2-frameTolerance:
            # keep track of start time/frame for later
            arrow.frameNStart = frameN  # exact frame index
            arrow.tStart = t  # local t and not account for scr refresh
            arrow.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(arrow, 'tStartRefresh')  # time at next scr refresh
            arrow.setAutoDraw(True)
        if arrow.status == STARTED:
            if bool(key_resp.status == FINISHED):
                # keep track of stop time/frame for later
                arrow.tStop = t  # not accounting for scr refresh
                arrow.frameNStop = frameN  # exact frame index
                win.timeOnFlip(arrow, 'tStopRefresh')  # time at next scr refresh
                arrow.setAutoDraw(False)
        
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
    answer_stop_time=tThisFlipGlobal
    trials.addData('problem0.started', problem0.tStartRefresh)
    trials.addData('problem0.stopped', problem0.tStopRefresh)
    trials.addData('problem1.started', problem1.tStartRefresh)
    trials.addData('problem1.stopped', problem1.tStopRefresh)
    trials.addData('problem2.started', problem2.tStartRefresh)
    trials.addData('problem2.stopped', problem2.tStopRefresh)
    trials.addData('problem6.started', problem6.tStartRefresh)
    trials.addData('problem6.stopped', problem6.tStopRefresh)
    trials.addData('problem7.started', problem7.tStartRefresh)
    trials.addData('problem7.stopped', problem7.tStopRefresh)
    trials.addData('answer.started', answer.tStartRefresh)
    trials.addData('answer.stopped', answer.tStopRefresh)
    trials.addData('answer1.started', answer1.tStartRefresh)
    trials.addData('answer1.stopped', answer_stop_time)
    trials.addData('answer2.started', answer2.tStartRefresh)
    trials.addData('answer2.stopped', answer_stop_time)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
        # was no response the correct answer?!
        if str(corrAns1).lower() == 'none':
           key_resp.corr = 1# correct non-response
        else:
           key_resp.corr = 0  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('key_resp.keys',key_resp.keys)
    trials.addData('key_resp.corr', key_resp.corr)
    if key_resp.keys != None:  # we had a response
        trials.addData('key_resp.rt', key_resp.rt)
    trials.addData('key_resp.started', key_resp.tStartRefresh)
    trials.addData('key_resp.stopped', answer_stop_time)
    trials.addData('fixation2.started', fixation2.tStartRefresh)
    trials.addData('fixation2.stopped', fixation2.tStopRefresh)
    trials.addData('fixation3.started', fixation3.tStartRefresh)
    trials.addData('fixation3.stopped', fixation3.tStopRefresh)
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys = None
        # was no response the correct answer?!
        if str(corrAns2).lower() == 'none':
           key_resp_4.corr = 1;  # correct non-response
        else:
           key_resp_4.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('key_resp_4.keys',key_resp_4.keys)
    trials.addData('key_resp_4.corr', key_resp_4.corr)
    trials.addData('corr', key_resp_4.corr+ key_resp.corr)
    totalCorrNum=totalCorrNum+key_resp_4.corr+ key_resp.corr
    if key_resp_4.keys != None:  # we had a response
        trials.addData('key_resp_4.rt', key_resp_4.rt)
    trials.addData('key_resp_4.started', key_resp_4.tStartRefresh)
    trials.addData('key_resp_4.stopped', answer_stop_time)
    trials.addData('fixation.started', fixation.tStartRefresh)
    trials.addData('fixation.stopped', fixation.tStopRefresh)
    trials.addData('arrow.started', arrow.tStartRefresh)
    trials.addData('arrow.stopped', answer_stop_time)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "middle_rest"-------
    continueRoutine = True
    # update component parameters for each repeat
    #if problem0.status == STARTED:
    #    port.setData(endMark)
    #    core.wait(0.05)
    #    port.setData(0)
    conpensate_time = 10.5-rand_t1-rand_t2-compensate_clock.getTime()#keep total time same
    # keep track of which components have finished
    middle_restComponents = [image_2, polygon_2]
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
        
        # *image_2* updates
        if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_2.frameNStart = frameN  # exact frame index
            image_2.tStart = t  # local t and not account for scr refresh
            image_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
            image_2.setAutoDraw(True)
        if image_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_2.tStartRefresh + conpensate_time-frameTolerance:
                # keep track of stop time/frame for later
                image_2.tStop = t  # not accounting for scr refresh
                image_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_2, 'tStopRefresh')  # time at next scr refresh
                image_2.setAutoDraw(False)
        
        # *polygon_2* updates
        if polygon_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_2.frameNStart = frameN  # exact frame index
            polygon_2.tStart = t  # local t and not account for scr refresh
            polygon_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_2, 'tStartRefresh')  # time at next scr refresh
            polygon_2.setAutoDraw(True)
        if polygon_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_2.tStartRefresh + conpensate_time-frameTolerance:
                # keep track of stop time/frame for later
                polygon_2.tStop = t  # not accounting for scr refresh
                polygon_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_2, 'tStopRefresh')  # time at next scr refresh
                polygon_2.setAutoDraw(False)
        
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

    polygon_2_stopTime=tThisFlipGlobal
    for thisComponent in middle_restComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('image_2.started', image_2.tStartRefresh)
    trials.addData('image_2.stopped', image_2.tStopRefresh)
    trials.addData('polygon_2.started', polygon_2.tStartRefresh)
    trials.addData('polygon_2.stopped', polygon_2_stopTime)
    # the Routine "middle_rest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 27.0 repeats of 'trials'


# ------Prepare to start Routine "end"-------
continueRoutine = True
routineTimer.add(10.000000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = [polygon]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *polygon* updates
    if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon.frameNStart = frameN  # exact frame index
        polygon.tStart = t  # local t and not account for scr refresh
        polygon.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
        polygon.setAutoDraw(True)
    if polygon.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > polygon.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            polygon.tStop = t  # not accounting for scr refresh
            polygon.frameNStop = frameN  # exact frame index
            win.timeOnFlip(polygon, 'tStopRefresh')  # time at next scr refresh
            polygon.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('polygon.started', polygon.tStartRefresh)
thisExp.addData('polygon.stopped', tThisFlipGlobal)
print("-"*80)
print(totalCorrNum)
print("-"*80)
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
