"""Bounded fraction-rule detection regressions for both checker consumers."""
import unittest

try:
    from . import check
except ImportError:
    import check

class FractionDetection(unittest.TestCase):
    def assert_rule(self,text: str,expected: bool) -> None:
        # Both production consumers must use the same bounded predicate.
        self.assertEqual(check._has_restricted_restoration_construct(text),expected,text)
        data=check._HBData()
        check._hb_scan_file('parts/p15/fixture.tex',text,data)
        self.assertEqual(bool(data.findings.get('rule-outside-registry')),expected,text)

    def test_numeric_quotient_followed_by_weak_convergence(self):
        self.assert_rule(r'\[\frac{S_n-n\mu}{\sigma\sqrt n}\Rightarrow\chi.\]',False)

    def test_nested_numeric_arguments_and_nested_fraction(self):
        self.assert_rule(r'\[\frac{{S_n-{n\mu}}}{\sqrt{\frac{n}{\mu}}}\Rightarrow\chi\]',False)

    def test_arrow_in_separated_paragraph_is_not_a_fraction_argument(self):
        self.assert_rule('\\[\\frac{1+a^2}{(t+a)^2}.\\]\n\n'
                         'This uses \\(X\\geq t\\Rightarrow X+a\\geq t+a\\).',False)

    def test_sequent_in_either_or_both_arguments(self):
        for text in [r'\frac{\Gamma\vdash A}{\Gamma\vdash B}',
                     r'\frac{p(s_0)}{\vdash p}',
                     r'\frac{\forall s(p(s)\Rightarrow q(s))}{p\leadsto q}']:
            with self.subTest(text=text):self.assert_rule(text,True)

    def test_nested_braces_and_escaped_braces_preserve_argument_extent(self):
        self.assert_rule(r'\frac{{\Gamma\vdash A}\quad\{B\}}{\Gamma\vdash C}',True)
        self.assert_rule(r'\frac{\#\{x:x>0\}}{n}\Rightarrow1',False)

    def test_long_premise_does_not_depend_on_240_character_window(self):
        self.assert_rule(r'\frac{'+'x '*250+r'\Gamma\vdash A}{\Gamma\vdash B}',True)

    def test_fraction_command_variants(self):
        for macro in ['frac','dfrac','tfrac','cfrac']:
            with self.subTest(macro=macro):
                self.assert_rule('\\'+macro+r'{a}{b}\Rightarrow\chi',False)
                self.assert_rule('\\'+macro+r'{\Gamma\vdash A}{\Gamma\vdash B}',True)
        self.assert_rule(r'\cfrac[l]{a}{b}\Rightarrow\chi',False)
        self.assert_rule(r'\cfrac[r]{\Gamma\vdash A}{\Gamma\vdash B}',True)

    def test_valid_unbraced_single_token_arithmetic(self):
        for text in [r'\frac 1n\Rightarrow0',r'\frac{1}n\Rightarrow0',
                     r'\frac 1{n}\Rightarrow0',r'\frac{a}\tau\Rightarrow0']:
            with self.subTest(text=text):self.assert_rule(text,False)

    def test_missing_or_unbalanced_arguments_fail_closed(self):
        for text in [r'\frac{a}',r'\frac{a}{b',r'\dfrac{a}{b',
                     r'\cfrac[l{a}{b}',r'\[\frac{a}\]',r'\frac']:
            with self.subTest(text=text):self.assert_rule(text,True)

    def test_explicit_rule_commands_remain_banned(self):
        self.assert_rule(r'\Rule{\Gamma\vdash A}{\Gamma\vdash B}',True)


if __name__ == '__main__':
    unittest.main()
