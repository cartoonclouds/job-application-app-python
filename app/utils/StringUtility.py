import inflection


class StringUtility:
    @staticmethod
    def upperToUnderscore(string: str) -> str:
        return "".join(
            "_" + char.lower() if char.isupper() else char for char in string
        ).lstrip("_")

    @staticmethod
    def columnerize(string: str) -> str:
        """
        Create the name of a table column.
        This method uses :func:`inflection.tableize` and the :func:`inflection.singularize`
        method on the last word in the string.

        Examples::

            >>> columnerize('RawScaledScorers')
            "raw_scaled_scorer"
            >>> columnerize('egg_and_ham')
            "egg_and_ham"
            >>> columnerize('fancyCategory')
            "fancy_category"
        """
        return inflection.singularize(inflection.tableize(string)).replace(" ", "_")
