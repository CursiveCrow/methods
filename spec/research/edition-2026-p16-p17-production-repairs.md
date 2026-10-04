# P16/P17: production repairs of accepted text

Recorded 7 September 2026 Pacific time, 8 September UTC. The scoped build uses the actual accepted finite-abduction and finite-preference chapters and their proofs, with the two actual P2 prerequisite fragments. The prior text acceptances remain historical evidence at their original hashes. This note identifies the later changes; an independent preservation review must bind them before carrying acceptance to current bytes.

## Maintained content identities

| File | Accepted text before production | Current production text |
| --- | --- | --- |
| `handbook/parts/p16/finite-abduction.tex` | `19E88AF8C80B63A7125FE61B3FE9CE192564CA02456A61020570AD4C6B7B9BC9` | `0F7D93E64D6EAB11CD2904C509DB168621ADB93D9D5A9AE3F448D62BF7E1C6B6` |
| `handbook/annex/p16/finite-abduction.tex` | `9965EE04CE9F0D7F9A6CC786CEE9355BC0E7B1403803A61AF745087C1C06D893` | `D027F796A1A887DD7217C412DDF95FAC42F69A34CCE4F1DCFECB224C76E1A4B4` |
| `handbook/parts/p17/finite-preferences.tex` | `58CFD946F16A9D068D0D81AF3262E26BBE926F87FFEF45C01CADD72E0DD0927C` | Unchanged |
| `handbook/annex/p17/finite-preferences.tex` | `DFA00CC716098DA6BF6076FEF0258A4180DD868358561AC56E12CF96B925D9DF` | `B141A371731E7A0A3BEFF1C88C839F98720BE4F894A2D475CAF098A61159202C` |

## Exact repairs and observed reasons

1. The P16 body had two uses of `\B`, and its annex had three. The macro is defined only inside inherited restoration scope. The actual build stopped at an undefined control sequence outside that scope. Each use now spells its existing expansion `\mathbb{B}`. The printed mathematical object is unchanged; the source guard was not weakened.

2. The build then stopped with `Improper \prevdepth` at a paragraph following an amsthm proof opening. Only the initial paragraph headings inside the affected proofs were changed to identical bold words followed by `\enspace`. The P16 headings are “Agreement with the book's semantics.”, “Qualified monotonicity.” and “Inconsistent background.”; the P17 headings are “Relations on alternatives.” and “Necessity.” The later paragraph headings remain as they were. Rebuilding verified that these changes remove the actual failure.

3. P16 body headers for `def:p16-abduction-two-tests` and `thm:p16-abduction-minimality` are followed by `\par\nobreak`, keeping each long heading with its text without changing the words.

4. One P16 citation locator changed from `prop.~2.1, manuscript p.~11` to `prop.~2.1, p.~11`, retaining its exact citation key, proposition and page. Removing the redundant word resolved the final 8.57-point overflow. Its cited artifact remains the undated Eiter–Gottlob manuscript, not an unverified journal version.

5. In the P16 annex, the same four candidate sets (empty, singleton a, singleton b, and the pair) and following period moved from inline mathematics to a display. No candidate or qualification changed.

6. Only the P16 body and annex input are wrapped in a local group with `\emergencystretch=1.5em` in their drivers. The part identity, headings and annex controls remain outside the group. The P17 drivers are unchanged. The two P2 prerequisite inputs receive the same local setting only in the internal QA driver, leaving maintained inherited content untouched.

The separate shared reference-kind correction is recorded in `edition-2026-editorial-reference-types.md` and independently reviewed there. No definition, theorem hypothesis, proof step, example value, source version or reference target was intentionally altered by these production repairs.

| Driver or dependency | Current SHA-256 |
| --- | --- |
| `handbook/parts/p16.tex` | `E6E476F0F0EAB035C28A3FCD964E0789C02250BE4D9E4B90DB8169F6558BEF8D` |
| `handbook/annex/p16.tex` | `42C1195029286D35850C346B06DB4705EB2595CB7308BA3553B03414E9D1A55E` |
| `handbook/parts/p17.tex` | `94B1A39026E95CECE627D0025CA86D6FA1F799712235A32F410A114B92F0D3F2` |
| `handbook/annex/p17.tex` | `CDFB2B0555402278C57DCBDCCD060D79BFEFA37186288DCEB73F503A92868F85` |
| `handbook/restoration/inherited-01661-01816.tex` | `FB12D36A183AC0FDF5C8B2F8A1BBC09238526FDB03F75364A6DC18239913EC3E` |
| `handbook/restoration/inherited-01817-01898.tex` | `499FEC700936D0625769D7C09AA2BC5FD1F6D976B9EAB1A9CBC8EDFE8CAFB9C4` |

The final scoped build and all 45 inspected pages are recorded in `spec/verification/edition-2026-p16-p17-scoped-production.md`. These are internal production checks; no final integrated PDF was replaced, and no formal unit admission or whole-part completion is granted here.
