# KCM SIMULATOR — Web-Based 1→C→0 Collapse Demonstration  
Version: v0.1  
Author: Saurabh Misra (Karnav)

---

## 1. OVERVIEW  
The **KCM Simulator** provides a visual, interactive demonstration of the  
**Karnav Collapse Model (KCM)**.

It shows how any input moves from:

Wave-State (1) → Collapse-State (C) → Center-State (0)

through:

- KRP Roots (MR, RR, TR, TmR)  
- Instability → Contradiction buildup  
- Stability scoring  
- Collapse classification  
- Energy model E(x) = D(x) + C(x)

This is a simplified UI for understanding the core behaviour of KCM.

---

## 2. FILES

### **ui_v0.1.html**  
The interactive front-end:
- input field  
- parameter sliders  
- collapse button  
- live results  

### **collapse_demo.js**  
Implements:
- KRP Root processing  
- stability score  
- contradiction model  
- collapse energy  
- collapse classification (Stable / Semi / Unstable)

### **signals.json**  
Sample scenarios for future simulator versions.

---

## 3. HOW TO RUN  
Open the UI file directly in a browser:

simulator/ui_v0.1.html

No server required.

---

## 4. HOW THE SIMULATOR WORKS (LOGIC FLOW)

Input → KRP Roots → Instability → Stability Score → D(x) + C(x) energy → Collapse classification

Breakdown:

### 1. KRP Roots  
- Meaning clarity  
- Route options  
- Structural trust  
- Time pressure  

### 2. Instability  
Higher instability = higher contradiction C(x)

### 3. Stability Score  
Average of:
- MR  
- TR  
- (100 - instability)  
- (100 - time-pressure)

### 4. Collapse Math

D(x) = |stability_score − 50| C(x) = instability / 2 E(x) = D(x) + C(x)

### 5. Collapse Classification  
- Stable Centered Collapse  
- Semi-Stable Collapse  
- Unstable / Premature Collapse  

---

## 5. FUTURE UPGRADE PLAN  
- Real-time graph of D(x), C(x), E(x)  
- 2D zeta-field simulator (RH demo)  
- Time-evolution animation of collapse  
- Node-link collapse visualization  
- KRP weight tuning UI  

---

## 6. STATUS  
This simulator is a pedagogical tool demonstrating  
**the functional essence of KCM.**

For formal math, see `/spec`.  
For executable backend, see `/engine`.

---

**End of simulator/README.md**


---
