# Medical & Regulatory Notice — Multi-Layer Brain Twin (MLBT)

**Version 1.0 — July 2026**
**Author: Sarah LAZRI**

---

## ⚠️ Preliminary Disclaimer

This document is an informational notice intended to define the boundaries of use for the Multi-Layer Brain Twin (MLBT) during its pilot phase. **It does not constitute legal advice.** Any deployment involving real health data must be reviewed by legal counsel specialized in health law and data protection, and, where applicable, undergo formal regulatory certification (medical device CE marking, health-data hosting certification, etc.).

---

## 1. Scope of Authorized Use

### 1.1 Software Status
The MLBT is currently distributed as a **pilot / research version**. It is:
- **Not a certified medical device** (no CE / FDA marking),
- **Not clinically validated** for autonomous diagnostic or therapeutic use,
- **Not intended to replace professional medical judgment**.

### 1.2 Authorized Uses During the Pilot Phase
- Methodological research and algorithmic exploration
- Simulation on synthetic or anonymized data
- Technical testing by partners under NDA
- Feasibility assessment for specific use cases

### 1.3 Explicitly Excluded Uses
- Autonomous clinical decision-making without supervision from a licensed healthcare professional
- Processing of real, identifiable health data outside a validated contractual and regulatory framework
- Clinical production deployment without applicable certification

---

## 2. Health Data Hosting Obligations

In accordance with the **French Public Health Code (Articles L.1111-8 et seq.)** and the HDS (Hébergeur de Données de Santé) certification framework, any personal health data processed, stored, or hosted in connection with real-world use of the MLBT must be:

- Hosted on **HDS-certified infrastructure** (the host itself certified, or the underlying technical subcontractor certified in the case of cascading hosting)
- Covered by a **hosting agreement** compliant with the certification framework's requirements (traceability, reversibility, business continuity/disaster recovery, physical and logical security)
- Compliant with the **GDPR**, in particular:
  - a defined legal basis for processing (consent, public interest, research, etc.)
  - data minimization
  - a defined retention period
  - data subject rights (access, rectification, erasure)
  - a record of processing activities and, where applicable, a Data Protection Impact Assessment (DPIA)

**As long as the MLBT is tested only on synthetic or anonymized data, the HDS obligation does not apply.** It becomes mandatory as soon as real health data, even pseudonymized, is processed.

---

## 3. Contractual Framework for Testers

Any partner or tester accessing the confidential MLBT engine must:

1. Sign a **Non-Disclosure Agreement (NDA)** beforehand
2. Sign, if real health data is involved, a **GDPR Data Processing Agreement (DPA)** specifying roles (data controller / processor)
3. Commit to using data only within the scope defined by the testing protocol
4. Guarantee that any infrastructure used to host real health data is HDS-certified (or equivalent — see Section 4bis for non-EU partners)

---

## 4. International Data Transfers (for non-EU partners)

If a testing partner is established outside the EU/EEA, any transfer of health-related data (even pseudonymized) out of the EU/EEA must comply with **GDPR Chapter V** on international transfers. In practice, one of the following safeguards must be in place before any data leaves the EU/EEA:

- **Standard Contractual Clauses (SCCs)** signed between the data exporter (EU-based) and the data importer (non-EU partner), or
- An **adequacy decision** from the European Commission covering the destination country, or
- **Binding Corporate Rules (BCRs)**, where applicable within a corporate group.

Additional requirements for non-EU pilot partners:

1. A **Data Processing Agreement (DPA)** must be signed alongside any NDA, clearly defining controller/processor roles.
2. The partner must confirm that any infrastructure used to host real health data meets a **security and confidentiality standard equivalent to HDS certification** (e.g., ISO 27001, ISO 27799, or local health-data hosting certification where one exists), even though HDS itself is a French-specific certification and does not formally apply outside France.
3. **Synthetic or fully anonymized data remain the default and preferred mode for cross-border pilot testing.** Real, identifiable health data should not be transferred internationally during the pilot phase unless all of the above safeguards are formally documented.
4. The pilot partner must designate a contact point responsible for data protection compliance on their side (e.g., a DPO or equivalent), where required by their local law.

**Disclaimer:** This section is a general compliance orientation, not legal advice. Cross-border health data transfer involves jurisdiction-specific rules (e.g., HIPAA in the US, PIPEDA in Canada) that must be assessed independently by qualified legal counsel in the partner's jurisdiction before any real data is shared.

---

## 5. Liability and Limitations

- The author of the MLBT provides no guarantee of clinical outcomes and disclaims any liability for use outside the scope defined in this notice.
- Results produced by the MLBT during the pilot phase are **exploratory only** and must be interpreted by a qualified professional.
- This notice will be updated as the project progresses toward clinical validation and regulatory certification phases.

---

## 6. Contact

For any question regarding authorized use, hosting requirements, or to initiate pilot access under NDA:

**Sarah LAZRI**
Contact: hello@sarahlazri.fr

---

*This document is subject to change. Any new version will be dated and versioned.*
