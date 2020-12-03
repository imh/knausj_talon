from talon import Module, Context, actions, ui, imgui, clip, settings

ctx = Context()
ctx.matches = r"""
mode: user.sql
mode: command 
and code.language: sql
"""
ctx.lists["user.code_functions"] = {
    "cast": "CAST",
    'distinct': "DISTINCT"
}


@ctx.action_class("user")
class user_actions:
    def code_insert_function(text: str, selection: str):
        if selection:
            text = text + "({})".format(selection)
        else:
            text = text + "()"

        actions.user.paste(text)
        actions.edit.left()
