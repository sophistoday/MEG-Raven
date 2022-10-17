/********************************************* 
 * Random-Dot-Not_Motion2Grid_Notloopv3 Test *
 *********************************************/

import { core, data, sound, util, visual } from './lib/psychojs-2021.2.3.js';
const { PsychoJS } = core;
const { TrialHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'random-dot-not_motion2Grid_notLoopV3';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001', 'runID': ''};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: false,
  color: new util.Color([0, 0, 0]),
  units: 'deg',
  waitBlanking: true
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(startRoutineBegin());
flowScheduler.add(startRoutineEachFrame());
flowScheduler.add(startRoutineEnd());
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin(trialsLoopScheduler));
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'start.png', 'path': 'start.png'},
    {'name': 'figure8.jpg', 'path': 'figure8.jpg'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var frameDur;
async function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2021.2.3';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var startClock;
var key_resp_3;
var start_image;
var restClock;
var fixation_1;
var trialClock;
var problem0;
var problem1;
var problem2;
var problem6;
var problem7;
var answer;
var answer1;
var answer2;
var key_resp;
var middle_restClock;
var conpensate;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "start"
  startClock = new util.Clock();
  key_resp_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  start_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'start_image', units : 'deg', 
    image : 'start.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [30, 20],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  /* Syntax Error: Fix Python code */
  // Initialize components for Routine "rest"
  restClock = new util.Clock();
  fixation_1 = new visual.Polygon ({
    win: psychoJS.window, name: 'fixation_1', units : 'height', 
    edges: 4, size:[0.2, 0.2],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.0, lineColor: new util.Color('crimson'),
    fillColor: new util.Color('crimson'),
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  problem0 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'problem0', units : 'deg', 
    image : 'run1/figure0_0.jpg', mask : undefined,
    ori : 0.0, pos : [(- 4.5), 0], size : [4, 4],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  problem1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'problem1', units : 'deg', 
    image : 'run1/figure0_1.jpg', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [4, 4],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  problem2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'problem2', units : 'deg', 
    image : 'run1/figure0_2.jpg', mask : undefined,
    ori : 0.0, pos : [4.5, 0], size : [4, 4],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  problem6 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'problem6', units : 'deg', 
    image : 'run1/figure0_6.jpg', mask : undefined,
    ori : 0.0, pos : [(- 4.5), 0], size : [4, 4],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  problem7 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'problem7', units : 'deg', 
    image : 'run1/figure0_7.jpg', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [4, 4],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  answer = new visual.ImageStim({
    win : psychoJS.window,
    name : 'answer', units : 'deg', 
    image : 'figure8.jpg', mask : undefined,
    ori : 0.0, pos : [4.5, 0], size : [4, 4],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -5.0 
  });
  answer1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'answer1', units : 'deg', 
    image : 'run1/target0_0.jpg', mask : undefined,
    ori : 0.0, pos : [(- 4.5), 0], size : [4, 4],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -7.0 
  });
  answer2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'answer2', units : 'deg', 
    image : 'run1/target0_0.jpg', mask : undefined,
    ori : 0.0, pos : [4.5, 0], size : [4, 4],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -8.0 
  });
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "middle_rest"
  middle_restClock = new util.Clock();
  conpensate = new visual.Polygon ({
    win: psychoJS.window, name: 'conpensate', units : 'height', 
    edges: 4, size:[0.2, 0.2],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.0, lineColor: new util.Color('crimson'),
    fillColor: new util.Color('crimson'),
    opacity: undefined, depth: -1, interpolate: true,
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var _key_resp_3_allKeys;
var startComponents;
function startRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'start'-------
    t = 0;
    startClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_3.keys = undefined;
    key_resp_3.rt = undefined;
    _key_resp_3_allKeys = [];
    if ((Number.parseInt(expInfo["runID"]) === 1)) {
        start_image.setImage("begin.png");
    } else {
        start_image.setImage("rest.png");
    }
    
    // keep track of which components have finished
    startComponents = [];
    startComponents.push(key_resp_3);
    startComponents.push(start_image);
    
    for (const thisComponent of startComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function startRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'start'-------
    // get current time
    t = startClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key_resp_3* updates
    if (t >= 0.2 && key_resp_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_3.tStart = t;  // (not accounting for frame time here)
      key_resp_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.clearEvents(); });
    }

    if (key_resp_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_3.getKeys({keyList: ['s'], waitRelease: false});
      _key_resp_3_allKeys = _key_resp_3_allKeys.concat(theseKeys);
      if (_key_resp_3_allKeys.length > 0) {
        key_resp_3.keys = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].name;  // just the last key pressed
        key_resp_3.rt = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *start_image* updates
    if (t >= 0.0 && start_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      start_image.tStart = t;  // (not accounting for frame time here)
      start_image.frameNStart = frameN;  // exact frame index
      
      start_image.setAutoDraw(true);
    }

    /* Syntax Error: Fix Python code */
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of startComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function startRoutineEnd() {
  return async function () {
    //------Ending Routine 'start'-------
    for (const thisComponent of startComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('key_resp_3.keys', key_resp_3.keys);
    if (typeof key_resp_3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_3.rt', key_resp_3.rt);
        routineTimer.reset();
        }
    
    key_resp_3.stop();
    port.setData(startMark);
    core.wait(0.05);
    port.setData(0);
    
    // the Routine "start" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var trials;
var currentLoop;
function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 18, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial of trials) {
      const snapshot = trials.getSnapshot();
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(restRoutineBegin(snapshot));
      trialsLoopScheduler.add(restRoutineEachFrame());
      trialsLoopScheduler.add(restRoutineEnd());
      trialsLoopScheduler.add(trialRoutineBegin(snapshot));
      trialsLoopScheduler.add(trialRoutineEachFrame());
      trialsLoopScheduler.add(trialRoutineEnd());
      trialsLoopScheduler.add(middle_restRoutineBegin(snapshot));
      trialsLoopScheduler.add(middle_restRoutineEachFrame());
      trialsLoopScheduler.add(middle_restRoutineEnd());
      trialsLoopScheduler.add(endLoopIteration(trialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}


var compensate_clock;
var restComponents;
function restRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'rest'-------
    t = 0;
    restClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    compensate_clock = new core.Clock();
    compensate_clock.reset;
    
    // keep track of which components have finished
    restComponents = [];
    restComponents.push(fixation_1);
    
    for (const thisComponent of restComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function restRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'rest'-------
    // get current time
    t = restClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fixation_1* updates
    if (t >= 0.0 && fixation_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixation_1.tStart = t;  // (not accounting for frame time here)
      fixation_1.frameNStart = frameN;  // exact frame index
      
      fixation_1.setAutoDraw(true);
    }

    frameRemains = 0.0 + (1.75 + (util.randint((- 1), 2) * 0.25)) - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fixation_1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fixation_1.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of restComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function restRoutineEnd() {
  return async function () {
    //------Ending Routine 'rest'-------
    for (const thisComponent of restComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "rest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var rand_t1;
var rand_t2;
var rand_idx;
var corrAns;
var _key_resp_allKeys;
var trialComponents;
function trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'trial'-------
    t = 0;
    trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    currentLoopNumber += 1;
    problem0.setImage((((("run" + run_lst[run_num].toString()) + "\\figure") + idx_final[[run_num, currentLoopNumber]].toString()) + "_0.jpg"));
    problem1.setImage((((("run" + run_lst[run_num].toString()) + "\\figure") + idx_final[[run_num, currentLoopNumber]].toString()) + "_1.jpg"));
    problem2.setImage((((("run" + run_lst[run_num].toString()) + "\\figure") + idx_final[[run_num, currentLoopNumber]].toString()) + "_2.jpg"));
    problem6.setImage((((("run" + run_lst[run_num].toString()) + "\\figure") + idx_final[[run_num, currentLoopNumber]].toString()) + "_3.jpg"));
    problem7.setImage((((("run" + run_lst[run_num].toString()) + "\\figure") + idx_final[[run_num, currentLoopNumber]].toString()) + "_4.jpg"));
    rand_t1 = (Number.parseInt(time_lst[[run_num, currentLoopNumber, 0]]) * 0.25);
    rand_t2 = (Number.parseInt(time_lst[[run_num, currentLoopNumber, 1]]) * 0.25);
    rand_idx = Number.parseInt(answer_lst[currentLoopNumber]);
    answer1.setImage((((((("run" + run_lst[run_num].toString()) + "/target") + idx_final[[run_num, currentLoopNumber]].toString()) + "_") + rand_idx.toString()) + ".jpg"));
    answer2.setImage((((((("run" + run_lst[run_num].toString()) + "/target") + idx_final[[run_num, currentLoopNumber]].toString()) + "_") + (1 - rand_idx).toString()) + ".jpg"));
    if ((rand_idx === 0)) {
        corrAns = "left";
    } else {
        corrAns = "right";
    }
    
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // keep track of which components have finished
    trialComponents = [];
    trialComponents.push(problem0);
    trialComponents.push(problem1);
    trialComponents.push(problem2);
    trialComponents.push(problem6);
    trialComponents.push(problem7);
    trialComponents.push(answer);
    trialComponents.push(answer1);
    trialComponents.push(answer2);
    trialComponents.push(key_resp);
    
    for (const thisComponent of trialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function trialRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'trial'-------
    // get current time
    t = trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *problem0* updates
    if (t >= 0.45 && problem0.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      problem0.tStart = t;  // (not accounting for frame time here)
      problem0.frameNStart = frameN;  // exact frame index
      
      problem0.setAutoDraw(true);
    }

    frameRemains = 0.45 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (problem0.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      problem0.setAutoDraw(false);
    }
    
    // *problem1* updates
    if (t >= 0.45 && problem1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      problem1.tStart = t;  // (not accounting for frame time here)
      problem1.frameNStart = frameN;  // exact frame index
      
      problem1.setAutoDraw(true);
    }

    frameRemains = 0.45 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (problem1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      problem1.setAutoDraw(false);
    }
    
    // *problem2* updates
    if (t >= 0.45 && problem2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      problem2.tStart = t;  // (not accounting for frame time here)
      problem2.frameNStart = frameN;  // exact frame index
      
      problem2.setAutoDraw(true);
    }

    frameRemains = 0.45 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (problem2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      problem2.setAutoDraw(false);
    }
    
    // *problem6* updates
    if (t >= (5.4 + rand_t1) && problem6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      problem6.tStart = t;  // (not accounting for frame time here)
      problem6.frameNStart = frameN;  // exact frame index
      
      problem6.setAutoDraw(true);
    }

    frameRemains = (5.4 + rand_t1) + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (problem6.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      problem6.setAutoDraw(false);
    }
    
    // *problem7* updates
    if (t >= (5.4 + rand_t1) && problem7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      problem7.tStart = t;  // (not accounting for frame time here)
      problem7.frameNStart = frameN;  // exact frame index
      
      problem7.setAutoDraw(true);
    }

    frameRemains = (5.4 + rand_t1) + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (problem7.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      problem7.setAutoDraw(false);
    }
    
    // *answer* updates
    if (t >= (5.4 + rand_t1) && answer.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      answer.tStart = t;  // (not accounting for frame time here)
      answer.frameNStart = frameN;  // exact frame index
      
      answer.setAutoDraw(true);
    }

    frameRemains = (5.4 + rand_t1) + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (answer.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      answer.setAutoDraw(false);
    }
    /* Syntax Error: Fix Python code */
    
    // *answer1* updates
    if (t >= ((10.4 + rand_t1) + rand_t2) && answer1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      answer1.tStart = t;  // (not accounting for frame time here)
      answer1.frameNStart = frameN;  // exact frame index
      
      answer1.setAutoDraw(true);
    }

    frameRemains = ((10.4 + rand_t1) + rand_t2) + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (answer1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      answer1.setAutoDraw(false);
    }
    
    // *answer2* updates
    if (t >= ((10.4 + rand_t1) + rand_t2) && answer2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      answer2.tStart = t;  // (not accounting for frame time here)
      answer2.frameNStart = frameN;  // exact frame index
      
      answer2.setAutoDraw(true);
    }

    frameRemains = ((10.4 + rand_t1) + rand_t2) + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (answer2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      answer2.setAutoDraw(false);
    }
    
    // *key_resp* updates
    if (t >= ((10.4 + rand_t1) + rand_t2) && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }

    frameRemains = ((10.4 + rand_t1) + rand_t2) + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (key_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_resp.status = PsychoJS.Status.FINISHED;
  }

    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['left', 'right'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        // was this correct?
        if (key_resp.keys == corrAns) {
            key_resp.corr = 1;
        } else {
            key_resp.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of trialComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trialRoutineEnd() {
  return async function () {
    //------Ending Routine 'trial'-------
    for (const thisComponent of trialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // was no response the correct answer?!
    if (key_resp.keys === undefined) {
      if (['None','none',undefined].includes(corrAns)) {
         key_resp.corr = 1;  // correct non-response
      } else {
         key_resp.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    psychoJS.experiment.addData('key_resp.corr', key_resp.corr);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var conpensate_time;
var middle_restComponents;
function middle_restRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'middle_rest'-------
    t = 0;
    middle_restClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    conpensate_time = (compensate_clock.getTime() % 1.5);
    
    // keep track of which components have finished
    middle_restComponents = [];
    middle_restComponents.push(conpensate);
    
    for (const thisComponent of middle_restComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function middle_restRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'middle_rest'-------
    // get current time
    t = middle_restClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *conpensate* updates
    if (t >= 0.0 && conpensate.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      conpensate.tStart = t;  // (not accounting for frame time here)
      conpensate.frameNStart = frameN;  // exact frame index
      
      conpensate.setAutoDraw(true);
    }

    frameRemains = 0.0 + conpensate_time - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (conpensate.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      conpensate.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of middle_restComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function middle_restRoutineEnd() {
  return async function () {
    //------Ending Routine 'middle_rest'-------
    for (const thisComponent of middle_restComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "middle_rest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
