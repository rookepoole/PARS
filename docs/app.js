
const stages = [
  {name:"PARSE", code:"CONTRACT_FREEZE", title:"Parse the real task.", copy:"Separate facts, assumptions, preferences, unknowns, prohibited paths, acceptance criteria, and the narrowest defensible claim.", input:"ambiguous request", output:"frozen contract + invariants"},
  {name:"BRANCH", code:"MECHANISM_DIVERSITY", title:"Branch into distinct mechanisms.", copy:"Explore genuinely different explanations or solution mechanisms instead of paraphrasing one idea. Preserve a NULL/OTHER branch when something unmodeled could matter.", input:"frozen problem state", output:"competing mechanisms + null"},
  {name:"TRANSFORM", code:"REPRESENTATION_SHIFT", title:"Expose hidden structure.", copy:"Change the representation when a different coordinate system, abstraction, decomposition, formalism, or encoding makes the problem easier to inspect or test.", input:"mechanism branches", output:"testable representations"},
  {name:"PERTURB", code:"HOSTILE_TEST", title:"Attack the leading answer.", copy:"Apply perturbations capable of breaking assumptions, provenance, robustness, constraints, or the apparent solution. A test that cannot hurt the idea is weak evidence.", input:"leading candidates", output:"failure pressure"},
  {name:"TEST", code:"DISCRIMINATING_EVIDENCE", title:"Prefer evidence that can change the decision.", copy:"Choose proof, counterexample, measurement, controlled experiment, held-out prediction, or another discriminating test over confidence or plausibility.", input:"competing predictions", output:"decision-relevant evidence"},
  {name:"RECONSTRUCT", code:"DEPENDENCY_REBUILD", title:"Rebuild after evidence changes.", copy:"Remove invalid influence, insert corrected evidence, recompute affected dependencies, rerun downstream checks, and preserve the failure history.", input:"changed evidence", output:"reconstructed state"},
  {name:"BUILD", code:"FINAL_MATERIALIZATION", title:"Build only after the gate passes.", copy:"Instantiate the exact final candidate, replay every active invariant, materialize the result, then replay any invariant the build step could have changed.", input:"verified candidate", output:"evidence-bounded result"}
];

const buttons = [...document.querySelectorAll(".stage")];
const els = {
  number:document.querySelector("#stage-number"), code:document.querySelector("#stage-code"),
  title:document.querySelector("#stage-title"), copy:document.querySelector("#stage-copy"),
  input:document.querySelector("#stage-input"), output:document.querySelector("#stage-output")
};

function selectEngineStage(i){
  const s=stages[i];
  buttons.forEach((b,j)=>{
    b.classList.toggle("active",i===j);
    b.setAttribute("aria-selected",i===j ? "true" : "false");
  });
  els.number.textContent=`STAGE 0${i+1}`;
  els.code.textContent=s.code;
  els.title.textContent=s.title;
  els.copy.textContent=s.copy;
  els.input.textContent=s.input;
  els.output.textContent=s.output;
}


buttons.forEach((b)=>b.addEventListener("click",()=>selectEngineStage(+b.dataset.stage)));
selectEngineStage(0);


const inv=document.querySelector("#toggle-invariant");
const gate=document.querySelector("#build-gate");
let failed=false;
inv.addEventListener("click",()=>{
  failed=!failed;
  inv.classList.toggle("pass",!failed);inv.classList.toggle("fail",failed);
  inv.querySelector("em").textContent=failed?"FAIL":"PASS";
  gate.classList.toggle("pass",!failed);gate.classList.toggle("fail",failed);
  gate.querySelector("span").textContent=failed?"BUILD BLOCKED / INVALID_FINAL_STATE":"BUILD AUTHORIZED";
  gate.querySelector("small").textContent=failed?"Return to Reconstruction or search.":"Click INV-003 to inject a failure.";
});

document.querySelectorAll("[data-copy]").forEach(btn=>btn.addEventListener("click",async()=>{
  const target=document.querySelector(btn.dataset.copy);
  try{await navigator.clipboard.writeText(target.innerText);btn.textContent="COPIED";setTimeout(()=>btn.textContent="COPY",1200)}
  catch{btn.textContent="SELECT";setTimeout(()=>btn.textContent="COPY",1200)}
}));

const observer=new IntersectionObserver(entries=>entries.forEach(e=>{if(e.isIntersecting)e.target.classList.add("visible")}),{threshold:.15});
document.querySelectorAll(".reveal").forEach(el=>observer.observe(el));


document.querySelectorAll(".mobile-menu a").forEach(link=>link.addEventListener("click",()=>{
  link.closest("details")?.removeAttribute("open");
}));


// v3.2 signature interaction: run a complete adversarial PARS pass.
const trace = document.querySelector("#pars-trace");
const breakBtn = document.querySelector("#hero-break");
const traceState = document.querySelector("#trace-state");
const traceMessage = document.querySelector("#trace-message");
const traceInv3 = document.querySelector("#trace-inv-3");
const traceVerdict = document.querySelector("#trace-verdict");
const traceVerdictCopy = document.querySelector("#trace-verdict-copy");
const traceStep = document.querySelector("#trace-step");
const traceProgress = document.querySelector("#trace-progress-fill");
const traceNodes = [...document.querySelectorAll(".trace-node")];

let traceBusy = false;
let traceTimers = [];

function clearTraceTimers(){
  traceTimers.forEach(clearTimeout);
  traceTimers = [];
}

function setTraceNode(index, mode="current"){
  traceNodes.forEach((node, i)=>{
    node.classList.remove("current","fail","rebuild");
    if(i < index) node.classList.add("done");
    else node.classList.remove("done");
  });
  if(index >= 0 && traceNodes[index]){
    traceNodes[index].classList.add(mode);
  }
}

function setInv3(status, mode=""){
  traceInv3.className = "";
  if(mode) traceInv3.classList.add(mode);
  traceInv3.innerHTML = `INV-003 <b>${status}</b>`;
}

function resetTrace(){
  clearTraceTimers();
  traceBusy = false;
  trace.classList.remove("is-broken","is-reconstructing");
  traceNodes.forEach(n=>n.classList.remove("current","done","fail","rebuild"));
  traceState.textContent = "READY FOR ADVERSARIAL RUN";
  traceMessage.textContent = "Run the complete PARS cycle. A hostile perturbation will break one invariant; Build must stay blocked until Reconstruction and retest repair the candidate.";
  setInv3("UNTESTED");
  traceVerdict.textContent = "PENDING";
  traceVerdictCopy.textContent = "run the adversarial pass";
  traceStep.textContent = "READY";
  traceProgress.style.width = "0%";
  breakBtn.disabled = false;
  breakBtn.textContent = "Break the claim";
}

function scheduleTrace(delay, fn){
  traceTimers.push(setTimeout(fn, delay));
}

function beginTrace(){
  if(traceBusy) return;
  resetTrace();
  traceBusy = true;
  breakBtn.disabled = true;
  breakBtn.textContent = "PARS running…";

  // 1 / PARSE
  scheduleTrace(200, ()=>{
    setTraceNode(0);
    traceStep.textContent = "01 / 09 · PARSE";
    traceProgress.style.width = "10%";
    traceState.textContent = "CONTRACT FROZEN";
    traceMessage.textContent = "Parse separates facts, assumptions, unknowns, prohibited paths, acceptance criteria, and the narrowest defensible claim.";
    traceVerdict.textContent = "PENDING";
    traceVerdictCopy.textContent = "contract established";
  });

  // 2 / BRANCH
  scheduleTrace(2000, ()=>{
    setTraceNode(1);
    traceStep.textContent = "02 / 09 · BRANCH";
    traceProgress.style.width = "21%";
    traceState.textContent = "BRANCHES OPEN";
    traceMessage.textContent = "Mechanism-distinct alternatives remain alive alongside NULL / OTHER so the leading explanation cannot win by default.";
    traceVerdictCopy.textContent = "alternatives preserved";
  });

  // 3 / TRANSFORM
  scheduleTrace(3800, ()=>{
    setTraceNode(2);
    traceStep.textContent = "03 / 09 · TRANSFORM";
    traceProgress.style.width = "32%";
    traceState.textContent = "STRUCTURE EXPOSED";
    traceMessage.textContent = "Transform changes the representation so assumptions, dependencies, and discriminating predictions can be inspected directly.";
    traceVerdictCopy.textContent = "candidate made testable";
  });

  // 4 / PERTURB
  scheduleTrace(5600, ()=>{
    setTraceNode(3);
    traceStep.textContent = "04 / 09 · PERTURB";
    traceProgress.style.width = "43%";
    traceState.textContent = "CONTRADICTION INJECTED";
    traceMessage.textContent = "A hostile perturbation targets INV-003. The candidate is challenged rather than protected by its earlier plausibility.";
    setInv3("CHALLENGED","challenge");
    traceVerdict.textContent = "CHALLENGED";
    traceVerdictCopy.textContent = "claim under adversarial pressure";
  });

  // 5 / TEST
  scheduleTrace(7600, ()=>{
    trace.classList.add("is-broken");
    setTraceNode(4,"fail");
    traceStep.textContent = "05 / 09 · TEST";
    traceProgress.style.width = "55%";
    traceState.textContent = "FAILURE CONFIRMED";
    traceMessage.textContent = "The discriminating test establishes that INV-003 fails. This is no longer a confidence issue: the candidate violates the contract.";
    setInv3("FAIL","fail");
    traceVerdict.textContent = "REJECTED";
    traceVerdictCopy.textContent = "candidate exceeds current evidence";
  });

  // 6 / FINAL GATE attempts Build and blocks it.
  scheduleTrace(9800, ()=>{
    setTraceNode(6,"fail");
    traceStep.textContent = "06 / 09 · FINAL GATE";
    traceProgress.style.width = "66%";
    traceState.textContent = "BUILD BLOCKED";
    traceMessage.textContent = "The Final Invariant Gate refuses Build. A failed active invariant cannot be overridden by branch confidence, aesthetics, or momentum.";
    traceVerdict.textContent = "WITHHELD";
    traceVerdictCopy.textContent = "delivery forbidden";
  });

  // 7 / RECONSTRUCT
  scheduleTrace(12100, ()=>{
    trace.classList.remove("is-broken");
    trace.classList.add("is-reconstructing");
    setTraceNode(5,"rebuild");
    traceStep.textContent = "07 / 09 · RECONSTRUCT";
    traceProgress.style.width = "77%";
    traceState.textContent = "RECONSTRUCTING";
    traceMessage.textContent = "Invalid influence is removed, affected dependencies are rebuilt, corrected evidence is inserted, and failure history is preserved.";
    setInv3("REPAIRING","retest");
    traceVerdict.textContent = "WITHHELD";
    traceVerdictCopy.textContent = "no stronger claim before retest";
  });

  // 8 / RETEST
  scheduleTrace(14500, ()=>{
    setTraceNode(4);
    traceStep.textContent = "08 / 09 · RETEST";
    traceProgress.style.width = "89%";
    traceState.textContent = "DOWNSTREAM REPLAY";
    traceMessage.textContent = "The repaired candidate is tested again. Every downstream check affected by the changed evidence must replay before Build can reopen.";
    setInv3("RETESTING","retest");
    traceVerdict.textContent = "PENDING";
    traceVerdictCopy.textContent = "verification replay in progress";
  });

  // 9 / BUILD
  scheduleTrace(17000, ()=>{
    trace.classList.remove("is-reconstructing");
    setTraceNode(6);
    traceStep.textContent = "09 / 09 · BUILD";
    traceProgress.style.width = "100%";
    traceState.textContent = "BUILD AUTHORIZED";
    traceMessage.textContent = "The repaired candidate now passes the demonstration invariants. Build may proceed, and the final claim remains bounded to what the evidence actually supports.";
    setInv3("PASS");
    traceVerdict.textContent = "SUPPORTED";
    traceVerdictCopy.textContent = "bounded to demonstrated evidence";
    breakBtn.disabled = false;
    breakBtn.textContent = "Replay the trace";
    traceBusy = false;
  });
}

breakBtn?.addEventListener("click", beginTrace);
resetTrace();

