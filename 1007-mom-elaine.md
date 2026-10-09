# Internal MOM — BOCIPT Pension Services, Wed 7 Oct 2026

Pre-workshop meeting with Elaine's team. About 87 minutes.

**Present:** Elaine (Head of Pension Services), Winkie (call centre), Ivy (PM), Emma (BT), me. Ken joined briefly by phone.

**Not present:** Karen (BT lead, wrote the funding slides), Angela (senior decision-maker), Clarence.

**Name caution:** the recording is noisy. Elaine, Winkie, Ivy, Emma and Ken are solid. Angela, Andrew and Clarence are my best reading — confirm the spelling before you repeat them.

---

## Key decisions

### 1. User groups cut to two

**Prospect** (public, not logged in) and **Member** (MPF, logged in). That is the whole audience.

- **ORSO is out.** Their operations are completely different from MPF, are company-specific, and raise confidentiality problems. No chatbot for ORSO.
- **Employer is out.**
- **Self-employed count as Members.** They want eMPF to handle their own affairs, same as everyone else.

This confirms and closes the open question in `layer-model.md`. The A4/A5 ORSO cells are dead. Drop them from the matrix.

### 2. The eMPF boundary is a hard no, not a soft preference

If a member insists on asking how to do something on the eMPF platform, **the bot does not answer**. It redirects, politely. Only very basic information can be given.

Reason: BOCIPT cannot answer on eMPF's behalf, and eMPF is the approver. Detailed operational steps are out.

This makes the routing layer (I4 in your notes) confirmed and mandatory. It is not a nice-to-have.

### 3. Link to forms by name, not by URL

Elaine's own evidence: she spent **two months** trying to find a TVC form. eMPF forms have no numbers, links change within about three months, and deep links get blocked by the site disclaimer.

Decision: **the bot names the form and tells the member where to find it. It does not hand out a deep link.**

Also: the bot should reach deeper entry points (specific forms, specific pages), **not sit at homepage level only**.

### 4. Level 3 soft promotion is the real strategic goal

This is the biggest thing in the meeting and it was not in the slides.

Management wants to test **soft push of BOCI products** through the bot, inside the sandbox. Quoted intent: test the effect of a soft push in a sandbox environment, then show MPFA how they would work with the bank.

Framed internally as **"digital surface capability"** — a persistent digital touchpoint that can:

- **Notify** members when new products launch. Concrete pain: My Choice added three funds this year and nobody noticed.
- **Capture leads with consent** before they open an account, so marketing can contact them later.
- **Retain** members who signal they want to leave or switch — answer well, but there is a hard line because the Trustee cannot sell.
- Eventually **cross-sell to Bank of China products**, if the bank wants the bot.

**Consent is a hard gate.** No proactive outreach without it. Their existing consent form covers marketing purposes, and it is group-level (BOC group), not just BOCIPT. Customer data cannot flow directly to the bank.

**This is your L3.** It is not a feature list. It is a commercial strategy that has to be validated with MPFA. Your existing framing — "we are asking the regulator whether a trustee may surface related products, and under what conditions" — is exactly right and now has management backing.

### 5. Fund comparison and performance projection are NOT in the sandbox

Karen's position, relayed in the room: fund comparison and projection belong to **phase 2**, not this sandbox.

Context: their existing fund comparison is a regulator-mandated PDF, ugly, and their website is described internally as "1980s". AQUMON-backed competitor tools are interactive. Also: an existing simulation tool on the site is **broken** — the last step cannot be clicked, Karen has reported it to Ken, nobody complained, so it stayed broken.

Useful for you: this kills the "make the graphics nicer" thread from the 2 Oct meeting and confirms the broken-tool evidence.

### 6. Roadmap before decisions — Elaine's explicit ask

Elaine will not commit to a target until she sees one:

> Show me a roadmap — what phase 1 GenAI can reach, what the add-value layer can reach. Then I can tell you where I want to go.

She also rejected pure copying: "I don't need to have what others have. I have my own reasons." Competitor tools (AIA, Manulife, Sun Life, all AQUMON-based) are reference, not target.

**Action for you:** build a simple capability roadmap, phase 1 / phase 2, before the 12th. This is now a prerequisite for getting a decision out of her.

### 7. Call-centre handoff must carry context

Real risk raised by the room: member spends an hour with the bot, bot fails, tells them to call, agent knows nothing, member repeats everything and is already angry.

A bank's AI bot project was cited as a cautionary tale — heavy investment, then still needed humans, and callers arrived already frustrated.

**Agreed direction:** give each chat session a **unique identifier**. The member quotes it when calling; the agent looks it up on a dashboard and sees the conversation.

CSI sells a call-centre module that handles this. **They are not buying it.** So the session-ID approach is the cheap substitute. Flag this to CSI as a requirement.

Also agreed: the bot should **not** encourage calling in every situation. Depends on the case. If the numbers show the bot is working, pull back the hotline prompt — but do not let the bot die either.

### 8. Knowledge base = their existing PDFs, verbatim

Confirmed working method:

- PS supplies PDFs of guidelines, internal procedures, SOPs and call scripts.
- The bot answers **only** from those documents.
- It does not invent. If it cannot find the document, it says it does not know.
- Example given in the room: if a document says 7 days, the bot says 7 days, not 6 or 8.

Also: **Vivian's existing education materials will be reused.** SFC-approved. They want a wording expert to refine them — optimisation must not change the compliance meaning.

**Action:** ask PS for the PDF set and for Vivian's materials, by name.

### 9. Accuracy will be measured by a joint golden test set

Agreed in the room: **30 to 50 questions**, roughly half straightforward ("happy") and half edge cases ("tricky"). PS and us build it **together**. This is the acceptance measure.

**Action:** make this a named workshop output, with an owner and a date.

### 10. Chatbot language — open, with a known gap

Site has Traditional Chinese and English. Question raised: should the bot follow the site language, or be independently selectable?

Direction: the bot can reply in the language asked, including Simplified Chinese, and point back to the Traditional Chinese page. **But the website has no Simplified Chinese**, so redirects land on a mismatched page. A web revamp is needed and **nobody is available to do it**.

Leave this open. Note it as a known limitation for the MPFA presentation, not as a decision.

### 11. Three-layer escalation model already blessed

Someone in the room (Andrew, per my reading) has already seen and approved a three-layer model:

1. Layer 1 — basic / low-likelihood questions
2. Layer 2 — things the bot can handle
3. Layer 3 — escalate to a human for tricky cases, including eMPF-platform tricky cases

He said OK. **Use this structure in the workshop.** It is already socially approved, so it costs nothing to adopt and it gives the room a familiar frame.

---

## The governance problem — read this twice

This is the most important non-technical finding.

- Karen wrote the 10 funding slides. **PS never properly reviewed them.** Said openly in the room: "we rushed out with ten-odd use cases you never looked at carefully."
- **Angela, the senior decision-maker, does not know what the project actually is.** Said repeatedly and by more than one person: "I really don't think she knows", "I also think she doesn't know", "she'll get it wrong".
- The decision on which use cases go forward **belongs to Angela**. Not Karen, not Ivy, not us. Quoted: "the choice is Angela's, it won't be Ivy's or Jensen's."
- Clarence's view: it is too rushed, too fast. Unfinished conversations need finishing first.
- **PS and BT must sit down and go through the list line by line before it goes up.** That has not happened.
- **Ken and Emily are completely buried** and Karen says do not rely on them for this.
- Karen's own advice to us: **cut the scope down**.

**What this means for you.** You cannot get a final scope decision on 12 Oct. The room can produce a *recommendation*. The decision is Angela's, and Angela is not briefed. Plan for that. Your 12 Oct output should be shaped as something that can be carried straight into a conversation with Angela — a menu with Must Have / Good to Have marked, not a finished spec.

Karen's frame for the menu, already stated: **pick one from Level 1, maybe two from Level 2, and think about Level 3.**

---

## Revised schedule

| Date | What | Notes |
| --- | --- | --- |
| **Mon 12 Oct, 9:00** | Requirements workshop. Design-thinking format. | Confirmed, proceeding. PS sends people who have input. **Output: mark Must Have and Good to Have against the menu.** Karen's view: if that is done, the presentation passes and the sandbox is fine. |
| Mon 19 Oct | Public holiday (their words) | Nothing |
| **Tue 20 Oct** | Workshop demo / rehearsal to the bosses | **The only free slot.** Small group: us, Ivy, Clarence, PS. Treat it as a rehearsal for the 27th. |
| 21–23 Oct | Blocked | Clarence at audit, Elaine unavailable |
| **Tue 27 Oct** | Present to MPFA | Cyberport AISC also opens to them this day |

The gap between the 12th and the 27th contains exactly **one** rehearsal. That is the real constraint.

---

## What changed against our earlier notes

| Earlier assumption | Now |
| --- | --- |
| ORSO might be the cleanest pilot | **ORSO is out.** Explicitly excluded |
| Routing to eMPF is a high-value use case | **Confirmed, and stronger** — it is a hard boundary, not a feature |
| L3 soft promotion is sensitive and needs MPFA's view | **Still true, but now it is management's actual goal.** Frame it as the sandbox question, as planned |
| Deep links to forms | **No.** Name the form, do not link |
| Fund comparison / projection in scope | **Out.** Phase 2 |
| Elaine needs convincing | **She needs a roadmap first**, then she will state a target |
| We can close scope on 12 Oct | **No.** Angela decides, and she is not briefed |
| Cyberport GPUs are free | They secured 8 without pushback, but Cyberport AISC is expected to charge once it opens on the 27th, and it may be expensive |

---

## Actions

**Mine, before 12 Oct**

1. Build the **capability roadmap** — phase 1 GenAI, then add-value layer. Elaine will not commit without it.
2. Reshape the workshop output as a **menu**: Must Have / Good to Have, one L1, two L2, L3 to think about.
3. Adopt the **three-layer escalation model** as the frame. Already approved, free to use.
4. Prepare the **soft-promotion L3 framing** as a question for MPFA, not a feature.
5. Drop ORSO, employer, fund comparison and projection from all materials.

**Ask PS for**

6. The PDF set: guidelines, SOPs, internal procedures, call scripts.
7. Vivian's education materials.
8. Start the **golden test set** — 30 to 50 questions, half tricky. Joint work.
9. Real member questions from the last two weeks, in whatever form exists.

**Ask Ivy / Karen to drive**

10. **Brief Angela.** This is the critical path. If Angela is not briefed before the 20th, the 27th presentation is exposed.
11. **PS and BT sit together and go through the list line by line** before anything goes up.
12. Confirm who attends on the 20th, and who is empowered to mark Must Have.
13. Session unique identifier for call-centre handoff — put it to CSI as a requirement, since they are not buying the call-centre module.

---

## For the workshop

Open with the three-layer model and the two user groups. Both are already agreed, so the room starts from consent rather than debate.

Then the roadmap. Then the menu.

Expect the room to drift into the bank cross-sell and the competitor tools. Both are interesting and both are phase 2. Park them visibly.

The one thing to protect: **do not let the 12th end without Must Have / Good to Have marked.** That is the only output that survives the trip to Angela.
