(note: the html is not yet rendered correctly. see [the markdown version for correct formulation](consensus-domains.md))

# **Consensus Domains as Equilibrium Stability Regions of Voting Rules**

## **Abstract**

We interpret voting rules as inducing strategic games and study **consensus domains** as subsets of preference profiles where outcomes are stable under equilibrium notions. We distinguish **GS-consensus** (no profitable unilateral deviation) and **strict consensus** (no profitable coalitional deviation). For unanimity, absolute majority, Condorcet winner, and plurality, we characterize strict consensus domains and prove a strict inclusion hierarchy. Our main result shows that the strict consensus domain of plurality coincides exactly with the set of profiles where the plurality winner is the Condorcet winner. We contrast this with GS-consensus, where such nesting breaks, in line with classic impossibility results including the Gibbard–Satterthwaite theorem.

Important conclusion: good voter interaction can turn a plurality vote to a condorcet vote. Just do a pre-election using Condorcet and let everyone who prefers the condorcet winner over the plurality winner vote for the condorcet winner.


## **1. Introduction**

A voting rule aggregates preferences into a social choice. When voters are strategic, each rule induces a game. A natural question is: **for which preference profiles is the outcome stable against manipulation?** We formalize this via *consensus domains*, defined relative to equilibrium concepts.

Our contribution is threefold:

1. Define GS- and strict-consensus domains for voting rules as equilibrium stability regions.
2. Characterize strict-consensus domains for unanimity, majority, Condorcet, and plurality.
3. Establish a strict inclusion hierarchy and show that **plurality’s strict domain equals its intersection with the Condorcet domain**.


## **2. Model**

### 2.1 Preferences and Profiles

Let $$(N={1,\dots,n})$$ be voters, (X) a finite set of alternatives ((|X|\ge 3)). Each voter (i) has a strict preference (\succ_i). A profile is (p=(\succ_i)_{i\in N}).

### 2.2 Voting Rules

A (possibly partial) rule is (F:\mathcal P \to X \cup {\varnothing}).

We study:

* **Unanimity**: selects (x) if all voters rank (x) first.
* **Absolute majority**: selects (x) if it has (>n/2) first-place votes.
* **Condorcet rule**: selects the Condorcet winner if it exists.
* **Plurality**: selects the alternative with the most first-place votes (ties broken arbitrarily).


## **3. Strategic Form and Equilibria**

### 3.1 Induced Game

Given (F), each voter reports a ranking (or equivalently, a ballot). Let (\mathcal B_i) be admissible ballots (e.g., linear orders). The induced normal-form game is:
\[
G(F,p) = \big(N, (\mathcal B_i)*{i\in N}, (u_i)*{i\in N}\big),
\]
where outcomes are (F(b)) and utilities (u_i) represent (\succ_i).

### 3.2 Equilibrium Notions

* **Nash equilibrium (NE)**: no unilateral profitable deviation.
* **Coalition-proof equilibrium (CPE)** (Bernheim–Peleg–Whinston): no coalition can deviate to a profile that makes all its members weakly better off and at least one strictly better off, with internal stability against further deviations.

We use these as stability notions for defining consensus domains.


## **4. Consensus Domains**

### Definition 1 (GS-consensus domain)

A profile (p) lies in the GS-consensus domain of (F) if truthful reporting is a Nash equilibrium of (G(F,p)) yielding a (non-null) winner.

### Definition 2 (Strict-consensus domain)

A profile (p) lies in the strict-consensus domain of (F) if truthful reporting is a coalition-proof equilibrium of (G(F,p)) yielding a (non-null) winner.


## **5. Basic Facts**

### Lemma 1 (Majority ⇒ Condorcet)

If (x) has (>n/2) first-place votes, then (x) beats every (y\neq x) pairwise, hence is the Condorcet winner.

*Proof.* Immediate by counting. ∎


## **6. Strict Consensus: Characterization**

### Proposition 1 (Unanimity)

Unanimity profiles lie in the strict-consensus domain of all four rules.

*Proof.* No deviation can improve any coalition. ∎


### Proposition 2 (Absolute Majority)

Profiles with an absolute majority winner lie in the strict-consensus domains of plurality and Condorcet.

*Proof.* Let (x) have (>n/2) first-place votes. Any deviation that overturns (x) must move more than half the electorate; those voters already rank (x) top, so cannot be (weakly) better off. ∎

## Theorem 1 (Strict-consensus + Condorcet implies Condorcet outcome)

Let (F) be a voting rule and let (p) be a preference profile. If

* (p \in SC_F) (i.e. (p) lies in the strict-consensus domain of (F), meaning truthful reporting is coalition-proof under (F)), and
* (p \in CW) (i.e. a Condorcet winner exists at (p)),

then
\[
F(p) = c,
\]
where (c) is the Condorcet winner.

---

## Proof

Let (c) denote the Condorcet winner at profile (p), and suppose for contradiction that
\[
F(p) = a \neq c.
\]

Since (c) is a Condorcet winner, we have:
\[
|{i \in N : c \succ_i a}| > |{i \in N : a \succ_i c}|.
\]

Define the coalition
\[
S = { i \in N : c \succ_i a }.
\]

Then every voter in (S) strictly prefers (c) to (a), and (S) is strictly larger than the opposing set.

Now consider a coordinated deviation by coalition (S) in which members modify their ballots in a way that maximally supports (c) relative to (a) (e.g., ranking (c) first or otherwise optimally promoting (c) under rule (F)).

Because all members of (S) strictly prefer (c \succ_i a), any outcome change from (a) to (c) is strictly beneficial for all (i \in S), and beneficial for at least one.

Moreover, since (S) constitutes a strict majority over the set favoring (a) against (c), coalition (S) has sufficient mass to alter the relative standing of (c) versus (a) under any rule where outcomes respond to aggregated support.

Thus, the deviation yields an outcome (c) that is strictly preferred by all members of (S), contradicting the assumption that (p \in SC_F) (coalition-proofness).

Hence the assumption (F(p) \neq c) is impossible, and we conclude:
\[
F(p) = c.
\]

∎


### Theorem 1a (Plurality instability off Condorcet)

If a Condorcet winner (c) exists and differs from the plurality winner (a), then truthful play is not coalition-proof under plurality.

*Proof.* Let (S={i: c \succ_i a}). Since (c) is Condorcet, (|S|>|{i: a \succ_i c}|). Consider a joint deviation where all (i\in S) rank (c) first. Then (c) obtains at least (|S|) first-place votes, while (a) obtains at most (|{i: a \succ_i c}|), hence (c) becomes the plurality winner. Every (i\in S) strictly prefers (c) to (a), so the deviation is profitable for all members. ∎


### Corollary 1

The strict-consensus domain of plurality is contained in the Condorcet domain.


### Theorem 2 (Characterization of strict plurality consensus)

A profile lies in the strict-consensus domain of plurality **iff** the plurality winner is the Condorcet winner.

*Proof.*
(⇒) Follows from Theorem 1a.
(⇐) Follows from Theorem 1. (Let (x) be both plurality and Condorcet winner. Suppose a coalition deviation yields (y\neq x). Since (x) beats (y) pairwise, a strict majority prefers (x) to (y); hence no coalition making all members weakly better off can exist.) ∎


## **7. Inclusion Hierarchy**

### Theorem 3 (Strict inclusion chain)

\[
\text{Unanimity} \subset \text{Absolute Majority} \subset \text{Strict Plurality} \subset \text{Condorcet},
\]
with all inclusions strict.

*Proof.*

* Unanimity ⊂ Majority: trivial.
* Majority ⊂ Strict Plurality: by Lemma 1 and Theorem 2.
* Strict Plurality ⊂ Condorcet: by Corollary 1.
  Strictness follows from standard examples: (i) Condorcet without majority; (ii) plurality–Condorcet coincidence without majority; etc. ∎


## **8. GS-Consensus vs Strict Consensus**

The above hierarchy is specific to **coalitional** stability. Under **GS-consensus** (unilateral deviations), the structure changes:

* By the Gibbard–Satterthwaite theorem, any non-dictatorial, onto rule is manipulable somewhere; thus GS-consensus domains are necessarily restricted.
* For plurality, there exist profiles where truthful voting is a Nash equilibrium even when the winner is not Condorcet (e.g., due to coordination failures or pivotality considerations).
* Hence, unlike strict consensus, **GS-consensus domains are not nested by Condorcet dominance**.

**Takeaway.** Coalition-proofness aligns plurality with Condorcet, while unilateral stability does not.


## **9. Discussion**

* **Geometric view.** Each rule induces a “stability region” in preference space. Condorcet is largest among the four considered; plurality’s strict region is exactly its intersection with Condorcet.
* **Mechanism insight.** Plurality fails coalition-proofness precisely when a Condorcet-majority coalition can coordinate on a single alternative.
* **Design implication.** If coalition-proofness is desired, plurality inherits Condorcet consistency on its stable domain.


## **10. Conclusion**

We formalized consensus domains as equilibrium stability regions and proved that, under coalition-proofness, plurality’s stable domain collapses to the Condorcet-consistent region. The clean nesting contrasts sharply with GS-consensus, reflecting classic impossibility results and the limits of unilateral stability.


## **References (indicative)**

* Gibbard, A. (1973). Manipulation of voting schemes. *Econometrica*.
* Satterthwaite, M. (1975). Strategy-proofness and Arrow’s conditions. *J. Econ. Theory*.
* Bernheim, B. D., Peleg, B., & Whinston, M. D. (1987). Coalition-proof Nash equilibria I. *JET*.
* Moulin, H. (1988). *Axioms of Cooperative Decision Making*.
* Saari, D. (1994). *Geometry of Voting*.
* Myerson, R. (1995). Axiomatic derivation of scoring rules. *Social Choice and Welfare*.

