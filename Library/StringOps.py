from robot.api.deco import keyword


class StringOps:

    @keyword
    def join_two_strings(self, arg1: str, arg2: str) -> str:
        return arg1 + " CPT " + arg2
