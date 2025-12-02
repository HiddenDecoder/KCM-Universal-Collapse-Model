# CONTRIBUTING GUIDELINES  
### Karnav Collapse Model (KCM)  
**Creator:** Saurabh Misra (Karnav)

---

## 1. PURPOSE  
This document defines the rules and standards for contributing to the  
**Karnav Collapse Model (KCM)** repository.

The goal is to maintain:
- conceptual integrity  
- mathematical correctness  
- architectural consistency  
- versioning discipline  
- respect for the creator’s model intentions  

All contributions must follow these guidelines.

---

## 2. GENERAL PRINCIPLES

### ✅ 1. Preserve the Core Structure  
KCM has a fixed architecture:

0–1–C Law → C-State Core → KRP Roots → Collapse Math → Engine/Simulator

No contribution may break or contradict this flow.

---

### ✅ 2. Respect the Creator’s Definitions  
All terminology (Collapse, C-State, MeaningRoot, etc.) must stay consistent  
with the official specifications in `/spec`.

---

### ✅ 3. No New Axioms  
Any mathematical or conceptual extension must be derived from existing KCM laws.  
No contributor may introduce new axioms or assumptions outside the framework.

---

### ✅ 4. Avoid Over-speculation  
All contributions must be:
- analytic  
- structural  
- mathematical  
- computational  

No philosophical or imaginative extrapolation is allowed.

---

## 3. CONTRIBUTION TYPES

### **1. Documentation Improvements**  
Allowed when:
- clarification is needed  
- readability improvements  
- missing links or diagrams  

Submit via Pull Request (PR).

---

### **2. Mathematical Enhancements**  
Allowed when:
- aligns with Collapse Math  
- provides deeper proofs  
- improves definitions  
- strengthens RH mapping  

Must include:
- derivations  
- definitions  
- references  
- notation consistency  

---

### **3. Engine Code Contributions**  
Must follow:
- PEP8 Python standard  
- modular architecture  
- separation of KRP and Collapse Math  
- no hard-coded magic values  
- documented logic in comments  

Every code PR must include:
- purpose  
- changes  
- tests (if applicable)

---

### **4. Simulator Contributions**  
Allowed if:
- improves UI  
- enhances collapse animations  
- adds graphs/visuals  
- integrates backend logic better  

No speculative behaviour.

---

## 4. WHAT IS NOT ALLOWED

### ❌ 1. Structural changes that break the model  
For example:
- removing C-State  
- modifying 0–1–C  
- altering collapse law  
- adding new states  

Not permitted.

---

### ❌ 2. Unsupported mathematical claims  
Every math claim must be:
- derived  
- justified  
- consistent  

No vague or ungrounded statements.

---

### ❌ 3. Unverified PRs  
Any PR without explanation or testable logic is rejected automatically.

---

### ❌ 4. Conceptual drift  
Model terminology must stay aligned with `/spec`.

---

## 5. VERSIONING RULES

KCM uses semantic versioning:

v0.x → experimental or early-stage
v1.x → stable theoretical structure
v2.x → validated by simulations

### Paper versions:

paper v0.x → draft
paper v1.x → preprint
paper v2.x → peer-reviewed

---

## 6. HOW TO SUBMIT A CONTRIBUTION

1. Fork the repository  
2. Create a feature branch  
3. Make changes  
4. Document changes  
5. Submit PR  
6. PR will be reviewed for:
   - structure  
   - math correctness  
   - consistency  
   - stability  

---

## 7. ISSUE REPORTING

Open issues ONLY for:
- documentation improvements  
- mathematical inconsistencies  
- engine logic bugs  
- UI bugs  
- clarity requests  

Irrelevant or speculative issues will be closed.

---

## 8. CITATION GUIDELINES

When referencing KCM in research or other projects, use:

Saurabh Misra (Karnav). “Karnav Collapse Model (KCM).” https://github.com/<your-repo>

(Add DOI once released.)

---

## 9. AUTHORITY STATEMENT  
The KCM model is the intellectual property and creation of **Saurabh Misra (Karnav)**.  
All contributions must respect the original structure and model coherence.

---

**End of CONTRIBUTING.md**


---
