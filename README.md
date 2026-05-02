# I2OS Resonance Extrapolation

## From Interpolation to Extrapolation

### A Minimal Resonance-Based Experiment

---

## 🔍 Overview

This repository demonstrates a minimal experiment showing that:

> Extrapolation depends on structure, not data volume.

Traditional machine learning models perform well within training data but fail outside it.

This project shows that **structure-preserving (resonance-based) representations** enable extrapolation beyond the training domain.

---

## 🧠 Core Idea

Baseline:
Data fitting → interpolation

Resonance:
Structure encoding → extrapolation

---

## ⚙️ I2OS Perspective

I = (∇M) ⊗ R

* ∇M : structural gradient
* R   : resonance

Meaning:

Intelligence = structure × resonance

---

## 🧪 Experiment

Target function:

y = sin(x) + 0.3 sin(3x)

Training:
x ∈ [0,6]

Extrapolation:
x ∈ [6,10]

---

## 🤖 Models

Baseline:
y = ax + b

Resonance:
φ(x) = [sin(x), cos(x), sin(2x), cos(2x), sin(3x), cos(3x)]

---

## 📊 Results

* Baseline fails in extrapolation
* Resonance preserves structure

---

## ▶️ How to Run

pip install numpy matplotlib scikit-learn
python code/experiment.py

---

## 👤 Author

Masayuki Ando

---

## 📜 License

MIT License
