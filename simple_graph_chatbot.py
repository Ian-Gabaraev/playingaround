"""
                                                       hey
                                                        |
                                                      hello
                                                        |
                                                   what is up?
                                                 /            \
                                      are you ok?              what are you doing?
                                     /                                            \
                      yes, thank you!                                              just chilling, you?
                                                                                  /                   \
                                                                            gaming                     reading
                                                                           /                                  \
                                                                 what game?                                   what book?
                                                               /        |                                     /
                                                      witcher 3      titan-fall 2                     catch-22
"""

from collections import deque


class UserSaying:

    def __init__(self, content):
        self.content = content

    def __str__(self):
        return self.content


class ChatBotSaying:

    def __init__(self, content):
        self.content = content

    def __str__(self):
        return self.content


hey = UserSaying("hey!")
bye = UserSaying("bye!")
morning = UserSaying("morning!")
what_is_up = UserSaying("sup?")
r_u_ok = UserSaying("are you ok?")
what_are_you_doing = UserSaying("what are you doing?")
gaming = UserSaying("gaming")
reading = UserSaying("reading")
witcher = UserSaying("witcher 3")
titan_fall = UserSaying("titan-fall 2")
catch = UserSaying("catch-22")

hello = ChatBotSaying("hello!")
see_you = ChatBotSaying("see you!")
is_it = ChatBotSaying("is it?")
not_much = ChatBotSaying("not much, thanks!")
yes_thanks = ChatBotSaying("I've seen better times, but thanks for asking!")
just_chilling = ChatBotSaying("just chilling, you?")
what_game = ChatBotSaying("what game?")
what_book = ChatBotSaying("what book?")
witcher_my_fav = ChatBotSaying("witcher 3 is my absolute favorite!")
titan_fall_sucks = ChatBotSaying("can't believe you are actually enjoying that...")

conversation_graph = {
    None: [hey, bye, morning],
    hey: [hello],
    bye: [see_you],
    morning: [is_it],
    hello: [what_is_up],
    what_is_up: [not_much],
    not_much: [r_u_ok, what_are_you_doing],
    r_u_ok: [yes_thanks],
    what_are_you_doing: [just_chilling],
    just_chilling: [gaming, reading],
    gaming: [what_game],
    reading: [what_book],
    what_game: [witcher, titan_fall],
    what_book: [catch],
    witcher: [witcher_my_fav],
    titan_fall: [titan_fall_sucks]
}


conversation = deque()
context = None
conversation += conversation_graph[context]


def reset(conversation_deque, context_object):
    conversation_deque.clear()
    conversation_deque += conversation_graph[context_object]


while conversation:

    user_said = input(">>>")
    option = conversation.popleft()

    try:
        while str(option) != user_said:
            option = conversation.popleft()
    except IndexError:
        print("Sorry, did not quite catch that.")
        reset(conversation, context)
    else:
        answer = conversation_graph[option][0]
        print(answer)
        conversation.clear()
        context = answer

        try:
            conversation += conversation_graph[context]
        except KeyError:
            print("End of conversation tree, resetting.")
            reset(conversation, None)
