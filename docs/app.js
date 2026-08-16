
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
  input:document.querySelector("#stage-input"), output:document.querySelector("#stage-output"),
  heroState:document.querySelector("#hero-state"), heroSub:document.querySelector("#hero-substate")
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

function selectHeroStage(i){
  const s=stages[i];
  els.heroState.textContent=s.name;
  els.heroSub.textContent=s.copy;
}

buttons.forEach((b)=>b.addEventListener("click",()=>selectEngineStage(+b.dataset.stage)));
selectEngineStage(0);
selectHeroStage(0);

let heroIndex=0;
const heroInstrument=document.querySelector(".hero-instrument");
let heroPaused=false;
heroInstrument?.addEventListener("mouseenter",()=>heroPaused=true);
heroInstrument?.addEventListener("mouseleave",()=>heroPaused=false);
heroInstrument?.addEventListener("focusin",()=>heroPaused=true);
heroInstrument?.addEventListener("focusout",()=>heroPaused=false);

setInterval(()=>{
  if(!document.hidden && !heroPaused){
    heroIndex=(heroIndex+1)%stages.length;
    selectHeroStage(heroIndex);
  }
},5000);

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
