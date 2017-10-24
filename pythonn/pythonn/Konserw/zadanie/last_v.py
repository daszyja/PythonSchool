
The first thing I notice is the deep nesting in infix_to_postfix. Deep nesting like that is generally undesirable. We'll get to that later.

Second, for the parenthesis, my instinct would be to say: "Use frozenset instead of set.". But after some benchmarking: set is actually fastest on my machine, so probably also on yours. (I also checked using a tuple instead, again slower than using a set). However, a more Pythonic declaration of the set would be PARENTHESIS = {"(", ")"}.

Regarding the regular expression and the method parse: it could be faster by using a compiled regex instead of using re.findall. Also, convention has it that you use raw strings for regular expressions.

REGEX = re.compile(r"(\d+|\w+|[-+*/^%()])")
def parse(e, REGEX=REGEX):
    return REGEX.findall(e)
The REGEX=REGEX trick is an optimization trick preventing a lookup to the global dictionary. Using compiled regular expressions also gains a bit of speed. (On the other hand: I don't see parse being used, so that's probably ok).

Since it's not documented, I'm going to assume the calling convention will be

postfix_tokens = infix_to_postfix(parse(infix_tokens)
Now, let's start analysing the large method infix_to_postfix. First of all, we could apply the same trick as we did for REGEX to speed up the lookup for OPERATORS. That's going to make your code a bit more efficient.

It's a tad large, so let's first talk about the if c in OPERATORS branch.

if len(stack) > 0:
    top = stack[-1]

    if top in OPERATORS.keys():
        if OPERATORS[c] > OPERATORS[top]:
            stack.append(c)
        else:
            while top in OPERATORS.keys() and OPERATORS[top] >= OPERATORS[c]:
                op = stack.pop()
                postfix.append(op)

                if len(stack) > 0:
                    top = stack[-1]
                else:
                    break
            stack.append(c)
    else:
        stack.append(c)
else:
    stack.append(c)
All these else conditions look the same. Let's see if we can simplify it a bit. Let's start by flipping the if and else branch in if OPERATORS[c] > OPERATORS[top]. (> becomes <=).

if len(stack) > 0:
    top = stack[-1]

    if top in OPERATORS.keys():
        if OPERATORS[c] <= OPERATORS[top]:
            while top in OPERATORS.keys() and OPERATORS[top] >= OPERATORS[c]:
                op = stack.pop()
                postfix.append(op)

                if len(stack) > 0:
                    top = stack[-1]
                else:
                    break
            stack.append(c)
        else:
            stack.append(c)
    else:
        stack.append(c)
else:
    stack.append(c)
Now, we have the following construct:

if cond:
    A()
    B()
 else:
    B()
Which we can rewrite to

if cond:
    A()
 B()
Applying that several times we get

if len(stack) > 0:
    top = stack[-1]

    if top in OPERATORS.keys():
        if OPERATORS[c] <= OPERATORS[top]:
            while top in OPERATORS.keys() and OPERATORS[top] >= OPERATORS[c]:
                op = stack.pop()
                postfix.append(op)

                if len(stack) > 0:
                    top = stack[-1]
                else:
                    break

stack.append(c)
Wow, we saved a few lines of code. If we're lucky, it's also going to gain us some performance.

Next, you have top in OPERATORS.keys(). This can be replaced by top in OPERATORS (as that's how dict containment checking works). Furthermore, len(stack) > 0 can be replaced by stack.

Furthermore, you write op = stack.pop() followed by postfix.append(op). You can simplify this to postfix.append(stack.pop()).

if stack:
    top = stack[-1]

    if top in OPERATORS:
        if OPERATORS[c] <= OPERATORS[top]:
            while top in OPERATORS and OPERATORS[top] >= OPERATORS[c]:
                postfix.append(stack.pop())

                if stack > 0:
                    top = stack[-1]
                else:
                    break

stack.append(c)
Let's continue our focus on the nested if top in OPERATORS. Now, for symmetry, we replace OPERATORS[c] <= OPERATORS[top] with OPERATORS[TOP] >= OPERATORS[C]. (I'm not showing the if stack: and stack.append(c) anymore).

if top in OPERATORS:
    if OPERATORS[top] >= OPERATORS[c]:
        while top in OPERATORS and OPERATORS[top] >= OPERATORS[c]:
            postfix.append(stack.pop())

            if stack > 0:
                top = stack[-1]
            else:
                break
We can merge the first two conditionals, because there are no else branches, using

if cond_a:
    if cond_b:
        ...
to

if cond_a and cond_b:
    ...
We get

if top in OPERATORS and OPERATORS[top] >= OPERATORS[c]:
    while top in OPERATORS and OPERATORS[top] >= OPERATORS[c]:
        postfix.append(stack.pop())

        if stack > 0:
            top = stack[-1]
        else:
            break
Now the similarity should be obvious, we can drop the if.

Zooming out again:

def infix_to_postfix(infix):
    stack = []
    postfix = []

    for c in infix:
        if c in OPERATORS:

            if stack:
                top = stack[-1]

                while top in OPERATORS and OPERATORS[top] >= OPERATORS[c]:
                    postfix.append(stack.pop())

                    if stack:
                        top = stack[-1]
                    else:
                        break

            stack.append(c)

        elif c in PARENTHESIS:

            if c == ")":
                if len(stack) > 0:
                    top = stack[-1]

                    while top != "(":
                        try:
                            # pop throws an IndexError if the list is empty
                            r = stack.pop()
                            postfix.append(r)  # Adding what's in between ( ) to the postfix list
                            top = stack[-1]
                        except IndexError:
                            raise ValueError("'(' not found when popping")

                    stack.pop()  # Removes ( from the top of the stack
                else:
                    raise ValueError("')' cannot be added to the stack if it is empty")
            else:
                stack.append(c)  # c == '('
        else:

            postfix.append(c)

        #print("Stack:", stack)
        #print("Postfix:", postfix)

    while len(stack) > 0:
        top = stack.pop()

        if top in OPERATORS.keys():
            postfix.append(top)

    return postfix
tekst = "((5 * 2) + 4) * ((3 * 2) + 1)"
infix_to_postfix(tekst)
