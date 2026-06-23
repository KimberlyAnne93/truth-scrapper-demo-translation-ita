python early:
    
    """
    Intended format:

    glossary character_glossary:
        title "Amour"
        subtitle "[Red-Haired, Dull, Helpful.]"

        text "{=sigmar}{color=5B8C63}PATH DWELLER / OUR GUIDE{/color}{/=sigmar} (she/he)"
        text "• Met on Day X-1. Agreed to guide us.\n"
        text "{=sigmar}{color=5B8C63}NOTES:{/color}{/=sigmar}"
        text "• Can ask her all the questions we want. Not likely to know much, though."
        if DayxAmourVain:
            text "• Vain. Compliment his face if you need something."

        image "charactermenu amour":
            xpos -430
            ypos -270
    """
    
    def parse_glossary_lines(ll, title, condition=None, previous_conditions=None, level=1):
        """A helper function which parses a series of glossary lines."""
        
        def subparse_cproperties(l, d):
            
            
            propname = l.name()
            if propname is not None:
                if propname in d: 
                    l.error("style property %s appears twice." % propname)
                
                d[propname] = l.require(l.simple_expression) 
                return True
            return False
        
        lines = []
        standalone = False
        
        kw = None
        previous_conditions = previous_conditions or {level:[ ]}
        
        if ll.keyword("if"):
            kw = "if"
            previous_conditions[level] = [ ]
        elif ll.keyword("elif"):
            kw = "elif"
        elif ll.keyword("else"):
            kw = "else"
        
        if kw:
            
            
            if kw in ("if", "elif"):
                current_condition = ll.delimited_python(":")
            else:
                current_condition = ""
            ll.require(":")
            ll.expect_eol()
            ll.expect_block("glossary condition block {}".format(current_condition))
            lll = ll.subblock_lexer()
            
            
            
            
            
            
            
            
            
            if kw == "if":
                
                previous_conditions[level].append(current_condition.strip())
                new_condition = current_condition.strip()
            elif kw == "elif":
                if not previous_conditions[level]:
                    ll.error("elif without preceding if in glossary entry {}".format(title))
                
                
                new_condition = " and ".join(["not ({})".format(c) for c in previous_conditions[level]] + [current_condition.strip()])
                previous_conditions[level].append(current_condition.strip())
            elif kw == "else":
                if not previous_conditions[level]:
                    ll.error("else without preceding if in glossary entry {}".format(title))
                
                new_condition = " and ".join(["not ({})".format(c) for c in previous_conditions[level]])
            
            
            
            
            
            
            if condition is not None and new_condition:
                new_condition = "({}) and ({})".format(condition, new_condition)
            
            
            while lll.advance():
                new_lines, previous_conditions = parse_glossary_lines(lll, title,
                    condition=new_condition, previous_conditions=previous_conditions, level=level+1)
                lines.extend(new_lines)
        
        
        
        standalone = False
        if ll.keyword("text"):
            keyword = 'text'
        elif ll.keyword("add"):
            keyword = 'add'
        elif ll.keyword("image"):
            keyword = 'image'
            standalone = True
        else:
            keyword = None
        
        if keyword:
            is_image = keyword in ('add', 'image')
            if keyword == 'text':
                
                start = ll.match("_\(")
                if start:
                    content = ll.require(ll.string)
                    ll.match("\)")
                else:
                    content = ll.require(ll.string)
            else:
                content = ll.require(ll.string)
            properties = {}
            
            
            
            
            while subparse_cproperties(ll, properties):
                pass
            
            if not ll.match(':'):
                
                ll.expect_noblock("glossary block {}".format(title))
                ll.expect_eol()
            else:
                
                ll.expect_block("glossary block {}".format(title))
                ll.expect_eol()
                
                lll = ll.subblock_lexer()
                
                
                while lll.advance():
                    while subparse_cproperties(lll, properties):
                        pass
                    lll.expect_eol()
            
            ll.expect_eol()
            
            lines.append(
                dict(content=content, is_image=is_image, standalone=standalone,
                    condition=condition, properties=properties)
            )
        
        return lines, previous_conditions
    
    
    def parse_glossary_entry(l):
        
        
        list_name = l.require(l.simple_expression)
        l.expect_block("glossary statement")
        ll = l.subblock_lexer()
        
        title = None
        page_title = None
        subtitle = None
        the_id = None
        keyword = None
        condition = None
        category = None
        previous_conditions = None
        
        lines = [ ]
        
        
        while ll.advance():
            
            if ll.keyword("title"):
                start = ll.match("_\(")
                if start:
                    title = ll.require(ll.string)
                    ll.match("\)")
                else:
                    title = ll.require(ll.string)
            
            if ll.keyword("page_title"):
                start = ll.match("_\(")
                if start:
                    page_title = ll.require(ll.string)
                    ll.match("\)")
                else:
                    page_title = ll.require(ll.string)
            
            if ll.keyword("subtitle"):
                start = ll.match("_\(")
                if start:
                    subtitle = ll.require(ll.string)
                    ll.match("\)")
                else:
                    subtitle = ll.require(ll.string)
            
            if ll.keyword("id"):
                start = ll.match("_\(")
                if start:
                    the_id = ll.require(ll.string)
                    ll.match("\)")
                else:
                    the_id = ll.require(ll.string)
            
            if ll.keyword("category"):
                start = ll.match("_\(")
                if start:
                    category = ll.require(ll.string)
                    ll.match("\)")
                else:
                    category = ll.require(ll.string)
            
            if ll.keyword("condition"):
                condition = ll.rest()
            
            
            new_lines, previous_conditions = parse_glossary_lines(ll, title,
                condition=None, previous_conditions=previous_conditions, level=1)
            lines.extend(new_lines)
        
        return dict(
            list_name=list_name, title=title, subtitle=subtitle, id=the_id,
            lines=lines, condition=condition, page_title=page_title,
            category=category,
        )
    
    def execute_glossary_entry(p):
        """
        Turn the provided lines into GlossaryLine objects and create a
        GlossaryEntry.
        """
        
        try:
            the_list = getattr(store, p["list_name"])
        except AttributeError:
            raise Exception("No list named {} found for glossary entry.".format(p["list_name"]))
        
        title = p['title']
        page_title = p['page_title']
        subtitle = p['subtitle']
        the_id = p['id']
        
        lines = [ ]
        images = [ ]
        
        
        for line in p['lines']:
            
            
            
            properties = {}
            for propname, propval in line['properties'].items():
                try:
                    properties[propname] = eval(propval)
                except Exception as e:
                    if config.developer:
                        raise Exception("Error evaluating property {} with value {} for glossary entry {}: {}".format(propname, propval, title, e))
                    else:
                        properties[propname] = propval
            if line['standalone']:
                images.append(GlossaryLine(
                    content=line['content'], is_image=line['is_image'],
                    condition=line['condition'], **properties))
            else:
                lines.append(GlossaryLine(
                    content=line['content'], is_image=line['is_image'],
                    condition=line['condition'], **properties))
        
        the_entry = GlossaryEntry(title, *lines, subtitle=subtitle, id=the_id,
            images=images, condition=p["condition"], page_title=page_title,
            category=p["category"])
        the_list.append(the_entry)
        
        return
    
    def translate_glossary_entry(p):
        """Return a list of strings that are available for translation."""
        title = p['title']
        page_title = p['page_title']
        subtitle = p['subtitle']
        category = p['category']
        to_translate = [ title ]
        if page_title:
            to_translate.append(page_title)
        if subtitle:
            to_translate.append(subtitle)
        if category:
            to_translate.append(category)
        for line in p['lines']:
            if not line['standalone'] and not line['is_image']:
                to_translate.append(line['content'])
        return to_translate
    
    renpy.register_statement("glossary", block=True,
        parse=parse_glossary_entry,
        
        execute=execute_glossary_entry,
        
        init=True,
        translation_strings=translate_glossary_entry,
        )

init python:
    
    
    
    
    
    
    
    
    
    
    class GlossaryEntry():
        """
        A class which holds information on a particular glossary entry.

        Attributes:
        -----------
        title : str
            The name of the entry.
        id : str
            A unique string used to identify this entry. If not provided, the
            title will be used, but lowercased and with spaces replaced by
            underscores.
        lines : list of GlossaryLine
            A list of lines which will be shown in the entry, in order. Each
            line can have a condition associated with it, and may include
            various style properties. It can include text or images.
        images : list of GlossaryLine
            A list of displayables which will be added to the entry. These
            may have a condition associated with them and can include various
            style properties. They are not shown in the same rows as the lines.
        subtitle : str
            A subtitle shown underneath the title on the entry page.
        page_title : str
            If provided, this is used instead of the title on the entry page.
        condition : str
            A string which can be evaluated to know whether this entry will be
            shown or not. If not provided, the entry will always be shown.
        category : str
            The heading under which this entry belongs in the glossary list.
            If not provided, the entry will have no heading.
        """
        def __init__(self, title, *lines, **kwargs):
            self.title = title
            self.page_title = kwargs.get("page_title") or self.title
            self.id = kwargs.get("id") or title.lower().replace(" ", "_")
            self.lines = lines
            self.images = kwargs.get("images", [])
            self.subtitle = kwargs.get("subtitle", None)
            self.condition = kwargs.get("condition", None)
            self.category = kwargs.get("category", None)
        
        def is_unlocked(self):
            """Return True if this entry can be viewed."""
            if self.condition is None:
                return True
            try:
                return eval(self.condition)
            except Exception as e:
                if config.developer:
                    raise e
                else:
                    return True
        
        def has_new_content(self):
            """
            Return True if this entry has content which was unlocked since
            it was last viewed.
            """
            new_content = False
            
            if self.id not in store.unlocked_entries:
                store.unlocked_entries[self.id] = {"lines": set(), "images": set()}
            
            
            for line in self.lines:
                if line.is_unlocked and line.condition is not None:
                    if line.condition not in store.unlocked_entries[self.id]["lines"]:
                        new_content = True
                    store.unlocked_entries[self.id]["lines"].add(line.condition)
            for image in self.images:
                if image.is_unlocked and image.condition is not None:
                    if image.condition not in store.unlocked_entries[self.id]["images"]:
                        new_content = True
                    store.unlocked_entries[self.id]["images"].add(image.condition)
            if new_content:
                return new_content
            
            if self.id not in store.read_entries:
                return True
            elif store.read_entries[self.id] != store.unlocked_entries[self.id]:
                return True
            return False
        
        def MarkRead(self):
            """
            Returns a screen action which will mark this entry as read.
            """
            return Function(self.mark_read)
        
        def mark_read(self):
            """Mark any new content in this entry as read."""
            
            store.read_entries[self.id] = {
                "images" : store.unlocked_entries[self.id]["images"].copy(),
                "lines" : store.unlocked_entries[self.id]["lines"].copy()
            }
    
    
    class GlossaryLine():
        """
        A class which holds information on a given line or image belonging to
        a GlossaryEntry.

        Attributes:
        -----------
        content : str or Displayable
            The text or displayable which will be shown in this line.
        is_image : bool
            True if the provided content is a displayable (and should be added
            via "add" instead of "text"), False if it's text.
        condition : str
            A string which can be evaluated to know whether this line will be
            shown or not. If not provided, the line will always be shown.
        properties : dict
            A dictionary of properties that will be applied to the line.
        """
        def __init__(self, content, is_image=False, condition=None, **properties):
            self.content = content
            self.is_image = is_image
            self.condition = condition.strip() if condition else None
            self.properties = properties
        
        @property
        def is_unlocked(self):
            """Return True if this line is visible."""
            if self.condition is None:
                return True
            try:
                return eval(self.condition)
            except Exception as e:
                if config.developer:
                    raise e
                else:
                    return True

default unlocked_entries = dict()
default read_entries = dict()

default test_condition = False
init python:
    
    
    test_glossary = [
        GlossaryEntry(
            "Test Entry",

            GlossaryLine("This is the first line."),
            GlossaryLine("This is the second line, which is only unlocked after a condition is met.", condition="test_condition"),
            GlossaryLine("This is the third line, which has some extra properties.", color="#ff0000"),
            GlossaryLine("TEST SUBTITLE", style="sigmar", color="#5B8C63"),
            GlossaryLine(None, height=50),
            GlossaryLine("This one is going to be long enough that I hope it'll wrap or something."),

            images=[
                GlossaryLine("charactermenu sosotte", is_image=True, xpos=-430, ypos=-250)
            ],
            subtitle="[[You, me, her, us. The person in the mirror.]",
        ),
        GlossaryEntry(
            "Second Entry",

            GlossaryLine("I would like to add images to this one"),
            GlossaryLine("gui/window_icon.png", is_image=True),
            GlossaryLine("That's all"),

        )
    ]

# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
