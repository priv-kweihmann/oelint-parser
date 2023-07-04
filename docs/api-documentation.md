# Table of Contents

* [oelint\_parser](#oelint_parser)
* [oelint\_parser.const\_vars](#oelint_parser.const_vars)
  * [set\_constantfile](#oelint_parser.const_vars.set_constantfile)
  * [set\_rulefile](#oelint_parser.const_vars.set_rulefile)
  * [get\_mandatory\_vars](#oelint_parser.const_vars.get_mandatory_vars)
  * [get\_suggested\_vars](#oelint_parser.const_vars.get_suggested_vars)
  * [get\_known\_mirrors](#oelint_parser.const_vars.get_known_mirrors)
  * [get\_protected\_vars](#oelint_parser.const_vars.get_protected_vars)
  * [get\_protected\_append\_vars](#oelint_parser.const_vars.get_protected_append_vars)
  * [get\_known\_vars](#oelint_parser.const_vars.get_known_vars)
  * [get\_known\_distros](#oelint_parser.const_vars.get_known_distros)
  * [get\_known\_machines](#oelint_parser.const_vars.get_known_machines)
  * [get\_image\_classes](#oelint_parser.const_vars.get_image_classes)
  * [get\_image\_variables](#oelint_parser.const_vars.get_image_variables)
  * [get\_base\_varset](#oelint_parser.const_vars.get_base_varset)
* [oelint\_parser.cls\_stash](#oelint_parser.cls_stash)
  * [Stash](#oelint_parser.cls_stash.Stash)
    * [\_\_init\_\_](#oelint_parser.cls_stash.Stash.__init__)
    * [AddFile](#oelint_parser.cls_stash.Stash.AddFile)
    * [Append](#oelint_parser.cls_stash.Stash.Append)
    * [Remove](#oelint_parser.cls_stash.Stash.Remove)
    * [GetRecipes](#oelint_parser.cls_stash.Stash.GetRecipes)
    * [GetLoneAppends](#oelint_parser.cls_stash.Stash.GetLoneAppends)
    * [GetLinksForFile](#oelint_parser.cls_stash.Stash.GetLinksForFile)
    * [GetItemsFor](#oelint_parser.cls_stash.Stash.GetItemsFor)
    * [ExpandVar](#oelint_parser.cls_stash.Stash.ExpandVar)
* [oelint\_parser.rpl\_regex](#oelint_parser.rpl_regex)
  * [RegexRpl](#oelint_parser.rpl_regex.RegexRpl)
    * [search](#oelint_parser.rpl_regex.RegexRpl.search)
    * [split](#oelint_parser.rpl_regex.RegexRpl.split)
    * [match](#oelint_parser.rpl_regex.RegexRpl.match)
    * [sub](#oelint_parser.rpl_regex.RegexRpl.sub)
    * [finditer](#oelint_parser.rpl_regex.RegexRpl.finditer)
* [oelint\_parser.const\_func](#oelint_parser.const_func)
* [oelint\_parser.inlinerep](#oelint_parser.inlinerep)
* [oelint\_parser.helper\_files](#oelint_parser.helper_files)
  * [get\_files](#oelint_parser.helper_files.get_files)
  * [get\_layer\_root](#oelint_parser.helper_files.get_layer_root)
  * [find\_local\_or\_in\_layer](#oelint_parser.helper_files.find_local_or_in_layer)
  * [get\_scr\_components](#oelint_parser.helper_files.get_scr_components)
  * [safe\_linesplit](#oelint_parser.helper_files.safe_linesplit)
  * [guess\_recipe\_name](#oelint_parser.helper_files.guess_recipe_name)
  * [guess\_base\_recipe\_name](#oelint_parser.helper_files.guess_base_recipe_name)
  * [guess\_recipe\_version](#oelint_parser.helper_files.guess_recipe_version)
  * [expand\_term](#oelint_parser.helper_files.expand_term)
  * [get\_valid\_package\_names](#oelint_parser.helper_files.get_valid_package_names)
  * [get\_valid\_named\_resources](#oelint_parser.helper_files.get_valid_named_resources)
  * [is\_image](#oelint_parser.helper_files.is_image)
  * [is\_packagegroup](#oelint_parser.helper_files.is_packagegroup)
* [oelint\_parser.constants](#oelint_parser.constants)
  * [Constants](#oelint_parser.constants.Constants)
    * [AddConstants](#oelint_parser.constants.Constants.AddConstants)
    * [RemoveConstants](#oelint_parser.constants.Constants.RemoveConstants)
    * [OverrideConstants](#oelint_parser.constants.Constants.OverrideConstants)
    * [AddFromRuleFile](#oelint_parser.constants.Constants.AddFromRuleFile)
    * [AddFromConstantFile](#oelint_parser.constants.Constants.AddFromConstantFile)
    * [FunctionsKnown](#oelint_parser.constants.Constants.FunctionsKnown)
    * [FunctionsOrder](#oelint_parser.constants.Constants.FunctionsOrder)
    * [VariablesMandatory](#oelint_parser.constants.Constants.VariablesMandatory)
    * [VariablesSuggested](#oelint_parser.constants.Constants.VariablesSuggested)
    * [MirrorsKnown](#oelint_parser.constants.Constants.MirrorsKnown)
    * [VariablesProtected](#oelint_parser.constants.Constants.VariablesProtected)
    * [VariablesProtectedAppend](#oelint_parser.constants.Constants.VariablesProtectedAppend)
    * [VariablesOrder](#oelint_parser.constants.Constants.VariablesOrder)
    * [VariablesKnown](#oelint_parser.constants.Constants.VariablesKnown)
    * [DistrosKnown](#oelint_parser.constants.Constants.DistrosKnown)
    * [MachinesKnown](#oelint_parser.constants.Constants.MachinesKnown)
    * [ImagesClasses](#oelint_parser.constants.Constants.ImagesClasses)
    * [ImagesVariables](#oelint_parser.constants.Constants.ImagesVariables)
    * [SetsBase](#oelint_parser.constants.Constants.SetsBase)
* [oelint\_parser.cls\_item](#oelint_parser.cls_item)
  * [Item](#oelint_parser.cls_item.Item)
    * [\_\_init\_\_](#oelint_parser.cls_item.Item.__init__)
    * [Line](#oelint_parser.cls_item.Item.Line)
    * [Raw](#oelint_parser.cls_item.Item.Raw)
    * [Links](#oelint_parser.cls_item.Item.Links)
    * [Origin](#oelint_parser.cls_item.Item.Origin)
    * [InFileLine](#oelint_parser.cls_item.Item.InFileLine)
    * [IncludedFrom](#oelint_parser.cls_item.Item.IncludedFrom)
    * [RealRaw](#oelint_parser.cls_item.Item.RealRaw)
    * [IsFromClass](#oelint_parser.cls_item.Item.IsFromClass)
    * [OverrideDelimiter](#oelint_parser.cls_item.Item.OverrideDelimiter)
    * [safe\_linesplit](#oelint_parser.cls_item.Item.safe_linesplit)
    * [get\_items](#oelint_parser.cls_item.Item.get_items)
    * [extract\_sub](#oelint_parser.cls_item.Item.extract_sub)
    * [extract\_sub\_func](#oelint_parser.cls_item.Item.extract_sub_func)
    * [IsFromAppend](#oelint_parser.cls_item.Item.IsFromAppend)
    * [AddLink](#oelint_parser.cls_item.Item.AddLink)
    * [GetAttributes](#oelint_parser.cls_item.Item.GetAttributes)
  * [Variable](#oelint_parser.cls_item.Variable)
    * [\_\_init\_\_](#oelint_parser.cls_item.Variable.__init__)
    * [VarName](#oelint_parser.cls_item.Variable.VarName)
    * [SubItem](#oelint_parser.cls_item.Variable.SubItem)
    * [SubItems](#oelint_parser.cls_item.Variable.SubItems)
    * [VarValue](#oelint_parser.cls_item.Variable.VarValue)
    * [VarOp](#oelint_parser.cls_item.Variable.VarOp)
    * [Flag](#oelint_parser.cls_item.Variable.Flag)
    * [VarNameComplete](#oelint_parser.cls_item.Variable.VarNameComplete)
    * [RawVarName](#oelint_parser.cls_item.Variable.RawVarName)
    * [VarValueStripped](#oelint_parser.cls_item.Variable.VarValueStripped)
    * [IsAppend](#oelint_parser.cls_item.Variable.IsAppend)
    * [AppendOperation](#oelint_parser.cls_item.Variable.AppendOperation)
    * [get\_items](#oelint_parser.cls_item.Variable.get_items)
    * [IsMultiLine](#oelint_parser.cls_item.Variable.IsMultiLine)
    * [GetDistroEntry](#oelint_parser.cls_item.Variable.GetDistroEntry)
    * [GetMachineEntry](#oelint_parser.cls_item.Variable.GetMachineEntry)
    * [GetClassOverride](#oelint_parser.cls_item.Variable.GetClassOverride)
  * [Comment](#oelint_parser.cls_item.Comment)
    * [\_\_init\_\_](#oelint_parser.cls_item.Comment.__init__)
    * [get\_items](#oelint_parser.cls_item.Comment.get_items)
  * [Include](#oelint_parser.cls_item.Include)
    * [\_\_init\_\_](#oelint_parser.cls_item.Include.__init__)
    * [IncName](#oelint_parser.cls_item.Include.IncName)
    * [Statement](#oelint_parser.cls_item.Include.Statement)
    * [get\_items](#oelint_parser.cls_item.Include.get_items)
  * [Export](#oelint_parser.cls_item.Export)
    * [\_\_init\_\_](#oelint_parser.cls_item.Export.__init__)
    * [Name](#oelint_parser.cls_item.Export.Name)
    * [Value](#oelint_parser.cls_item.Export.Value)
    * [get\_items](#oelint_parser.cls_item.Export.get_items)
  * [Function](#oelint_parser.cls_item.Function)
    * [\_\_init\_\_](#oelint_parser.cls_item.Function.__init__)
    * [IsPython](#oelint_parser.cls_item.Function.IsPython)
    * [IsFakeroot](#oelint_parser.cls_item.Function.IsFakeroot)
    * [FuncName](#oelint_parser.cls_item.Function.FuncName)
    * [FuncNameComplete](#oelint_parser.cls_item.Function.FuncNameComplete)
    * [SubItem](#oelint_parser.cls_item.Function.SubItem)
    * [SubItems](#oelint_parser.cls_item.Function.SubItems)
    * [FuncBody](#oelint_parser.cls_item.Function.FuncBody)
    * [FuncBodyStripped](#oelint_parser.cls_item.Function.FuncBodyStripped)
    * [FuncBodyRaw](#oelint_parser.cls_item.Function.FuncBodyRaw)
    * [GetDistroEntry](#oelint_parser.cls_item.Function.GetDistroEntry)
    * [GetMachineEntry](#oelint_parser.cls_item.Function.GetMachineEntry)
    * [IsAppend](#oelint_parser.cls_item.Function.IsAppend)
    * [get\_items](#oelint_parser.cls_item.Function.get_items)
  * [PythonBlock](#oelint_parser.cls_item.PythonBlock)
    * [\_\_init\_\_](#oelint_parser.cls_item.PythonBlock.__init__)
    * [FuncName](#oelint_parser.cls_item.PythonBlock.FuncName)
    * [get\_items](#oelint_parser.cls_item.PythonBlock.get_items)
  * [TaskAssignment](#oelint_parser.cls_item.TaskAssignment)
    * [\_\_init\_\_](#oelint_parser.cls_item.TaskAssignment.__init__)
    * [FuncName](#oelint_parser.cls_item.TaskAssignment.FuncName)
    * [VarValue](#oelint_parser.cls_item.TaskAssignment.VarValue)
    * [VarName](#oelint_parser.cls_item.TaskAssignment.VarName)
    * [get\_items](#oelint_parser.cls_item.TaskAssignment.get_items)
  * [FunctionExports](#oelint_parser.cls_item.FunctionExports)
    * [\_\_init\_\_](#oelint_parser.cls_item.FunctionExports.__init__)
    * [FuncNames](#oelint_parser.cls_item.FunctionExports.FuncNames)
    * [get\_items](#oelint_parser.cls_item.FunctionExports.get_items)
    * [get\_items\_unaliased](#oelint_parser.cls_item.FunctionExports.get_items_unaliased)
  * [TaskAdd](#oelint_parser.cls_item.TaskAdd)
    * [\_\_init\_\_](#oelint_parser.cls_item.TaskAdd.__init__)
    * [FuncName](#oelint_parser.cls_item.TaskAdd.FuncName)
    * [Before](#oelint_parser.cls_item.TaskAdd.Before)
    * [After](#oelint_parser.cls_item.TaskAdd.After)
    * [get\_items](#oelint_parser.cls_item.TaskAdd.get_items)
  * [MissingFile](#oelint_parser.cls_item.MissingFile)
    * [\_\_init\_\_](#oelint_parser.cls_item.MissingFile.__init__)
    * [Filename](#oelint_parser.cls_item.MissingFile.Filename)
    * [Statement](#oelint_parser.cls_item.MissingFile.Statement)
* [oelint\_parser.parser](#oelint_parser.parser)
  * [get\_full\_scope](#oelint_parser.parser.get_full_scope)
  * [prepare\_lines\_subparser](#oelint_parser.parser.prepare_lines_subparser)
  * [prepare\_lines](#oelint_parser.parser.prepare_lines)
  * [get\_items](#oelint_parser.parser.get_items)

<a id="oelint_parser"></a>

# oelint\_parser

<a id="oelint_parser.const_vars"></a>

# oelint\_parser.const\_vars

<a id="oelint_parser.const_vars.set_constantfile"></a>

#### set\_constantfile

```python
def set_constantfile(obj)
```

set constants

**Arguments**:

- `obj` _dict_ - dictionary with constants

<a id="oelint_parser.const_vars.set_rulefile"></a>

#### set\_rulefile

```python
def set_rulefile(obj)
```

set rules

**Arguments**:

- `obj` _dict_ - dictionary with rule definitions

<a id="oelint_parser.const_vars.get_mandatory_vars"></a>

#### get\_mandatory\_vars

```python
def get_mandatory_vars()
```

get mandatory variables

**Returns**:

- `list` - list of mandatory variable names

<a id="oelint_parser.const_vars.get_suggested_vars"></a>

#### get\_suggested\_vars

```python
def get_suggested_vars()
```

get suggested variables

**Returns**:

- `list` - list of suggested variable names

<a id="oelint_parser.const_vars.get_known_mirrors"></a>

#### get\_known\_mirrors

```python
def get_known_mirrors()
```

get known mirror replacements

**Returns**:

- `dict` - dictionary of known mirror replacements

<a id="oelint_parser.const_vars.get_protected_vars"></a>

#### get\_protected\_vars

```python
def get_protected_vars()
```

get protected variables

**Returns**:

- `list` - list of protected variables

<a id="oelint_parser.const_vars.get_protected_append_vars"></a>

#### get\_protected\_append\_vars

```python
def get_protected_append_vars()
```

get protected variables in bbappends

**Returns**:

- `list` - list of protected variables

<a id="oelint_parser.const_vars.get_known_vars"></a>

#### get\_known\_vars

```python
def get_known_vars()
```

get list of known variables

**Returns**:

- `list` - list of known variable names

<a id="oelint_parser.const_vars.get_known_distros"></a>

#### get\_known\_distros

```python
def get_known_distros()
```

get known distros

**Returns**:

- `list` - list of known distro names

<a id="oelint_parser.const_vars.get_known_machines"></a>

#### get\_known\_machines

```python
def get_known_machines()
```

get known machines

**Returns**:

- `list` - list of known machine names

<a id="oelint_parser.const_vars.get_image_classes"></a>

#### get\_image\_classes

```python
def get_image_classes()
```

get known classes used exclusively in an image

**Returns**:

- `list` - list of known class names

<a id="oelint_parser.const_vars.get_image_variables"></a>

#### get\_image\_variables

```python
def get_image_variables()
```

get known variables used exclusively in an image

**Returns**:

- `list` - list of known variable names

<a id="oelint_parser.const_vars.get_base_varset"></a>

#### get\_base\_varset

```python
def get_base_varset()
```

get variable baseset
Set includes basic package definitions

**Returns**:

- `dict` - base variable set

<a id="oelint_parser.cls_stash"></a>

# oelint\_parser.cls\_stash

<a id="oelint_parser.cls_stash.Stash"></a>

## Stash Objects

```python
class Stash()
```

<a id="oelint_parser.cls_stash.Stash.__init__"></a>

#### \_\_init\_\_

```python
def __init__(quiet=False)
```

constructor

<a id="oelint_parser.cls_stash.Stash.AddFile"></a>

#### AddFile

```python
def AddFile(_file, lineOffset=0, forcedLink=None)
```

Adds a file to the stash

**Arguments**:

- `_file` _str_ - Full path to file
  

**Arguments**:

- `lineOffset` _int_ - Line offset from the file that include this file (default: {0})
- `forcedLink` _type_ - Force link against a file (default: {None})
  

**Returns**:

- `list` - List of {oelint_parser.cls_item.Item}

<a id="oelint_parser.cls_stash.Stash.Append"></a>

#### Append

```python
def Append(item)
```

appends one or mote items to the stash

**Arguments**:

- `item` _Item_ - Item(s) to append

<a id="oelint_parser.cls_stash.Stash.Remove"></a>

#### Remove

```python
def Remove(item)
```

removes one or more items from the stash

**Arguments**:

- `item` _Item_ - Item(s) to remove

<a id="oelint_parser.cls_stash.Stash.GetRecipes"></a>

#### GetRecipes

```python
def GetRecipes()
```

Get bb files in stash

**Returns**:

- `list` - List of bb files in stash

<a id="oelint_parser.cls_stash.Stash.GetLoneAppends"></a>

#### GetLoneAppends

```python
def GetLoneAppends()
```

Get bbappend without a matching bb

**Returns**:

- `list` - list of bbappend without a matching bb

<a id="oelint_parser.cls_stash.Stash.GetLinksForFile"></a>

#### GetLinksForFile

```python
def GetLinksForFile(filename)
```

Get file which this file is linked against

**Arguments**:

- `filename` _str_ - full path to file
  

**Returns**:

- `list` - list of full paths the file is linked against

<a id="oelint_parser.cls_stash.Stash.GetItemsFor"></a>

#### GetItemsFor

```python
def GetItemsFor(filename=None,
                classifier=None,
                attribute=None,
                attributeValue=None,
                nolink=False)
```

Get items for filename

**Arguments**:

- `filename` _str_ - Full path to file (default: {None})
- `classifier` _str_ - class specifier (e.g. Variable) (default: {None})
- `attribute` _str_ - class attribute name (default: {None})
- `attributeValue` _str_ - value of the class attribute name (default: {None})
- `nolink` _bool_ - Consider linked files (default: {False})
  

**Returns**:

- `[type]` - [description]

<a id="oelint_parser.cls_stash.Stash.ExpandVar"></a>

#### ExpandVar

```python
def ExpandVar(filename=None,
              attribute=None,
              attributeValue=None,
              nolink=False)
```

Expand variable to dictionary

**Arguments**:

- `filename` _str_ - Full path to file (default: {None})
- `attribute` _str_ - class attribute name (default: {None})
- `attributeValue` _str_ - value of the class attribute name (default: {None})
- `nolink` _bool_ - Consider linked files (default: {False})
  

**Returns**:

- `{dict}` - expanded variables from call + base set of variables

<a id="oelint_parser.rpl_regex"></a>

# oelint\_parser.rpl\_regex

<a id="oelint_parser.rpl_regex.RegexRpl"></a>

## RegexRpl Objects

```python
class RegexRpl()
```

Safe regex replacements

<a id="oelint_parser.rpl_regex.RegexRpl.search"></a>

#### search

```python
@staticmethod
def search(pattern, string, timeout=5, default=None, *args, **kwargs)
```

replacement for re.search

**Arguments**:

- `pattern` _str_ - regex pattern
- `string` _str_ - input string
- `timeout` _int, optional_ - Timeout for operation. On timeout `default` will be returned. Defaults to 5.
- `default` __type_, optional_ - Default to return on timeout. Defaults to None.
  

**Returns**:

- `Match` - Match object or None

<a id="oelint_parser.rpl_regex.RegexRpl.split"></a>

#### split

```python
@staticmethod
def split(pattern, string, timeout=5, default=None, *args, **kwargs)
```

replacement for re.split

**Arguments**:

- `pattern` _str_ - regex pattern
- `string` _str_ - input string
- `timeout` _int, optional_ - Timeout for operation. On timeout `default` will be returned. Defaults to 5.
- `default` __type_, optional_ - Default to return on timeout. Defaults to None.
  

**Returns**:

- `list` - list object or None

<a id="oelint_parser.rpl_regex.RegexRpl.match"></a>

#### match

```python
@staticmethod
def match(pattern, string, timeout=5, default=None, *args, **kwargs)
```

replacement for re.match

**Arguments**:

- `pattern` _str_ - regex pattern
- `string` _str_ - input string
- `timeout` _int, optional_ - Timeout for operation. On timeout `default` will be returned. Defaults to 5.
- `default` __type_, optional_ - Default to return on timeout. Defaults to None.
  

**Returns**:

- `Match` - Match object or None

<a id="oelint_parser.rpl_regex.RegexRpl.sub"></a>

#### sub

```python
@staticmethod
def sub(pattern, repl, string, timeout=5, default='', *args, **kwargs)
```

replacement for re.sub

**Arguments**:

- `pattern` _str_ - regex pattern
- `repl` _str_ - replacement string
- `string` _str_ - input string
- `timeout` _int, optional_ - Timeout for operation. On timeout `default` will be returned. Defaults to 5.
- `default` __type_, optional_ - Default to return on timeout. Defaults to ''.
  

**Returns**:

- `str` - string

<a id="oelint_parser.rpl_regex.RegexRpl.finditer"></a>

#### finditer

```python
@staticmethod
def finditer(pattern, string, timeout=5, default=None, *args, **kwargs)
```

replacement for re.finditer

**Arguments**:

- `pattern` _str_ - regex pattern
- `string` _str_ - input string
- `timeout` _int, optional_ - Timeout for operation. On timeout `default` will be returned. Defaults to 5.
- `default` __type_, optional_ - Default to return on timeout. Defaults to None.
  

**Returns**:

- `Scanner` - Scanner object or None

<a id="oelint_parser.const_func"></a>

# oelint\_parser.const\_func

<a id="oelint_parser.inlinerep"></a>

# oelint\_parser.inlinerep

<a id="oelint_parser.helper_files"></a>

# oelint\_parser.helper\_files

<a id="oelint_parser.helper_files.get_files"></a>

#### get\_files

```python
def get_files(stash, _file, pattern)
```

Get files matching SRC_URI entries

**Arguments**:

- `stash` _oelint_parser.cls_stash.Stash_ - current stash
- `_file` _str_ - Full path to filename
- `pattern` _str_ - glob pattern to apply
  

**Returns**:

- `list` - list of files matching pattern

<a id="oelint_parser.helper_files.get_layer_root"></a>

#### get\_layer\_root

```python
def get_layer_root(name)
```

Find the path to the layer root of a file

**Arguments**:

- `name` _str_ - filename
  

**Returns**:

- `str` - path to layer root or empty string

<a id="oelint_parser.helper_files.find_local_or_in_layer"></a>

#### find\_local\_or\_in\_layer

```python
def find_local_or_in_layer(name, localdir)
```

Find file in local dir or in layer

**Arguments**:

- `name` _str_ - filename
- `localdir` _str_ - path to local dir
  

**Returns**:

- `str` - path to found file or None

<a id="oelint_parser.helper_files.get_scr_components"></a>

#### get\_scr\_components

```python
def get_scr_components(string)
```

Return SRC_URI components

**Arguments**:

- `string` _str_ - raw string
  

**Returns**:

- `dict` - scheme: protocol used, src: source URI, options: parsed options

<a id="oelint_parser.helper_files.safe_linesplit"></a>

#### safe\_linesplit

```python
def safe_linesplit(string)
```

Split line in a safe manner

**Arguments**:

- `string` _str_ - raw input
  

**Returns**:

- `list` - safely split input

<a id="oelint_parser.helper_files.guess_recipe_name"></a>

#### guess\_recipe\_name

```python
def guess_recipe_name(_file)
```

Get the recipe name from filename

**Arguments**:

- `_file` _str_ - filename
  

**Returns**:

- `str` - recipe name

<a id="oelint_parser.helper_files.guess_base_recipe_name"></a>

#### guess\_base\_recipe\_name

```python
def guess_base_recipe_name(_file)
```

Get the base recipe name from filename (aka BPN)

**Arguments**:

- `_file` _str_ - filename
  

**Returns**:

- `str` - recipe name

<a id="oelint_parser.helper_files.guess_recipe_version"></a>

#### guess\_recipe\_version

```python
def guess_recipe_version(_file)
```

Get recipe version from filename

**Arguments**:

- `_file` _str_ - filename
  

**Returns**:

- `str` - recipe version

<a id="oelint_parser.helper_files.expand_term"></a>

#### expand\_term

```python
def expand_term(stash, _file, value, spare=None, seen=None)
```

Expand a variable (replacing all variables by known content)

**Arguments**:

- `stash` _oelint_parser.cls_stash.Stash_ - current stash
- `_file` _str_ - Full path to file
- `value` _str_ - Variable value to expand
  

**Returns**:

- `str` - expanded value

<a id="oelint_parser.helper_files.get_valid_package_names"></a>

#### get\_valid\_package\_names

```python
def get_valid_package_names(stash, _file, strippn=False)
```

Get known valid names for packages

**Arguments**:

- `stash` _oelint_parser.cls_stash.Stash_ - current stash
- `_file` _str_ - Full path to file
  

**Returns**:

- `list` - list of valid package names

<a id="oelint_parser.helper_files.get_valid_named_resources"></a>

#### get\_valid\_named\_resources

```python
def get_valid_named_resources(stash, _file)
```

Get list of valid SRCREV resource names

**Arguments**:

- `stash` _oelint_parser.cls_stash.Stash_ - current stash
- `_file` _str_ - Full path to file
  

**Returns**:

- `list` - list of valid SRCREV resource names

<a id="oelint_parser.helper_files.is_image"></a>

#### is\_image

```python
def is_image(stash, _file)
```

returns if the file is likely an image recipe or not

**Arguments**:

- `stash` _oelint_parser.cls_stash.Stash_ - current stash
- `_file` _str_ - Full path to file
  

**Returns**:

- `bool` - True if _file is an image recipe

<a id="oelint_parser.helper_files.is_packagegroup"></a>

#### is\_packagegroup

```python
def is_packagegroup(stash, _file)
```

returns if the file is likely a packagegroup recipe or not

**Arguments**:

- `stash` _oelint_parser.cls_stash.Stash_ - current stash
- `_file` _str_ - Full path to file
  

**Returns**:

- `bool` - True if _file is a packagegroup recipe

<a id="oelint_parser.constants"></a>

# oelint\_parser.constants

<a id="oelint_parser.constants.Constants"></a>

## Constants Objects

```python
class Constants()
```

Interface for constants

<a id="oelint_parser.constants.Constants.AddConstants"></a>

#### AddConstants

```python
def AddConstants(_dict)
```

Add constants to the existing

**Arguments**:

- `dict` _dict_ - constant dictionary to add

<a id="oelint_parser.constants.Constants.RemoveConstants"></a>

#### RemoveConstants

```python
def RemoveConstants(_dict)
```

Remove constants from the existing

**Arguments**:

- `dict` _dict_ - constant dictionary to remove

<a id="oelint_parser.constants.Constants.OverrideConstants"></a>

#### OverrideConstants

```python
def OverrideConstants(_dict)
```

Override constants in the existing db

**Arguments**:

- `dict` _dict]_ - constant dictionary with override values

<a id="oelint_parser.constants.Constants.AddFromRuleFile"></a>

#### AddFromRuleFile

```python
def AddFromRuleFile(_dict)
```

Legacy interface to support rule files

**Arguments**:

- `dict` _dict_ - rule file dictionary

<a id="oelint_parser.constants.Constants.AddFromConstantFile"></a>

#### AddFromConstantFile

```python
def AddFromConstantFile(_dict)
```

Legacy interface to support constant files

**Arguments**:

- `dict` _dict_ - constant file dictionary

<a id="oelint_parser.constants.Constants.FunctionsKnown"></a>

#### FunctionsKnown

```python
@property
def FunctionsKnown()
```

Return known functions

**Returns**:

- `list` - list of known functions

<a id="oelint_parser.constants.Constants.FunctionsOrder"></a>

#### FunctionsOrder

```python
@property
def FunctionsOrder()
```

Return function order

**Returns**:

- `list` - List of functions to order in their designated order

<a id="oelint_parser.constants.Constants.VariablesMandatory"></a>

#### VariablesMandatory

```python
@property
def VariablesMandatory()
```

Return mandatory variables

**Returns**:

- `list` - List of mandatory variables

<a id="oelint_parser.constants.Constants.VariablesSuggested"></a>

#### VariablesSuggested

```python
@property
def VariablesSuggested()
```

Return suggested variables

**Returns**:

- `list` - List of suggested variables

<a id="oelint_parser.constants.Constants.MirrorsKnown"></a>

#### MirrorsKnown

```python
@property
def MirrorsKnown()
```

Return known mirrors and their replacements

**Returns**:

- `dict` - Dict of known mirrors and their replacements

<a id="oelint_parser.constants.Constants.VariablesProtected"></a>

#### VariablesProtected

```python
@property
def VariablesProtected()
```

Return protected variables

**Returns**:

- `list` - List of protected variables

<a id="oelint_parser.constants.Constants.VariablesProtectedAppend"></a>

#### VariablesProtectedAppend

```python
@property
def VariablesProtectedAppend()
```

Return protected variables in bbappend files

**Returns**:

- `list` - List of protected variables in bbappend files

<a id="oelint_parser.constants.Constants.VariablesOrder"></a>

#### VariablesOrder

```python
@property
def VariablesOrder()
```

Variable order

**Returns**:

- `list` - List of variables to order in their designated order

<a id="oelint_parser.constants.Constants.VariablesKnown"></a>

#### VariablesKnown

```python
@property
def VariablesKnown()
```

Known variables

**Returns**:

- `list` - List of known variables

<a id="oelint_parser.constants.Constants.DistrosKnown"></a>

#### DistrosKnown

```python
@property
def DistrosKnown()
```

Known distros

**Returns**:

- `list` - List of known distros

<a id="oelint_parser.constants.Constants.MachinesKnown"></a>

#### MachinesKnown

```python
@property
def MachinesKnown()
```

Known machines

**Returns**:

- `list` - List of known machines

<a id="oelint_parser.constants.Constants.ImagesClasses"></a>

#### ImagesClasses

```python
@property
def ImagesClasses()
```

Classes that are used in images

**Returns**:

- `list` - Classes that are used in images

<a id="oelint_parser.constants.Constants.ImagesVariables"></a>

#### ImagesVariables

```python
@property
def ImagesVariables()
```

Variables that are used in images

**Returns**:

- `list` - Variables that are used in images

<a id="oelint_parser.constants.Constants.SetsBase"></a>

#### SetsBase

```python
@property
def SetsBase()
```

Base variable set

**Returns**:

- `dict` - dictionary with base variable set

<a id="oelint_parser.cls_item"></a>

# oelint\_parser.cls\_item

<a id="oelint_parser.cls_item.Item"></a>

## Item Objects

```python
class Item()
```

Base class for all Stash items

<a id="oelint_parser.cls_item.Item.__init__"></a>

#### \_\_init\_\_

```python
def __init__(origin, line, infileline, rawtext, realraw)
```

constructor

**Arguments**:

- `origin` _str_ - Full path of origin file
- `line` _int_ - Overall line counter
- `infileline` _int_ - Line number in file
- `rawtext` _str_ - Raw input string (except inline code blocks)
- `realraw` _str_ - Unprocessed input

<a id="oelint_parser.cls_item.Item.Line"></a>

#### Line

```python
@property
def Line()
```

Overall line count

**Returns**:

- `int` - overall line count of item

<a id="oelint_parser.cls_item.Item.Raw"></a>

#### Raw

```python
@property
def Raw()
```

Raw string (without inline code blocks)

**Returns**:

- `str` - raw string of item

<a id="oelint_parser.cls_item.Item.Links"></a>

#### Links

```python
@property
def Links()
```

Linked files

**Returns**:

- `list` - list of full path of linked files

<a id="oelint_parser.cls_item.Item.Origin"></a>

#### Origin

```python
@property
def Origin()
```

origin of item

**Returns**:

- `str` - full path of origin file

<a id="oelint_parser.cls_item.Item.InFileLine"></a>

#### InFileLine

```python
@property
def InFileLine()
```

Line count in file

**Returns**:

- `int` - [description]

<a id="oelint_parser.cls_item.Item.IncludedFrom"></a>

#### IncludedFrom

```python
@property
def IncludedFrom()
```

Files include this item

**Returns**:

- `list` - list of files including this item

<a id="oelint_parser.cls_item.Item.RealRaw"></a>

#### RealRaw

```python
@property
def RealRaw()
```

Completely unprocessed raw text

**Returns**:

- `str` - completely unprocessed raw text

<a id="oelint_parser.cls_item.Item.IsFromClass"></a>

#### IsFromClass

```python
@property
def IsFromClass()
```

Item comes from a bbclass

**Returns**:

- `bool` - if item was set in a bbclass

<a id="oelint_parser.cls_item.Item.OverrideDelimiter"></a>

#### OverrideDelimiter

```python
@property
def OverrideDelimiter()
```

Override delimiter

**Returns**:

- `str` - Override delimiter

<a id="oelint_parser.cls_item.Item.safe_linesplit"></a>

#### safe\_linesplit

```python
@staticmethod
def safe_linesplit(string)
```

Safely split an input line to chunks

**Arguments**:

- `string` _str_ - raw input string
  

**Returns**:

- `list` - list of chunks of original string

<a id="oelint_parser.cls_item.Item.get_items"></a>

#### get\_items

```python
def get_items()
```

Return single items

**Returns**:

- `list` - lines of raw input

<a id="oelint_parser.cls_item.Item.extract_sub"></a>

#### extract\_sub

```python
def extract_sub(name)
```

Extract modifiers

**Arguments**:

- `name` _str_ - input string
  

**Returns**:

- `tuple` - clean variable name, modifiers, package specific modifiers

<a id="oelint_parser.cls_item.Item.extract_sub_func"></a>

#### extract\_sub\_func

```python
def extract_sub_func(name)
```

Extract modifiers for functions

**Arguments**:

- `name` _str_ - input value
  

**Returns**:

- `tuple` - clean function name, modifiers

<a id="oelint_parser.cls_item.Item.IsFromAppend"></a>

#### IsFromAppend

```python
def IsFromAppend()
```

Item originates from a bbappend

**Returns**:

- `bool` - True if coming from a bbappend

<a id="oelint_parser.cls_item.Item.AddLink"></a>

#### AddLink

```python
def AddLink(_file)
```

Links files to each other in stash

**Arguments**:

- `_file` _str_ - Full path of file to link against

<a id="oelint_parser.cls_item.Item.GetAttributes"></a>

#### GetAttributes

```python
def GetAttributes()
```

Get all public attributes of this class

**Returns**:

- `dict` - all public attributes and their values

<a id="oelint_parser.cls_item.Variable"></a>

## Variable Objects

```python
class Variable(Item)
```

Stash item for variables

<a id="oelint_parser.cls_item.Variable.__init__"></a>

#### \_\_init\_\_

```python
def __init__(origin, line, infileline, rawtext, name, value, operator, flag,
             realraw)
```

constructor

**Arguments**:

- `origin` _str_ - Full path to file of origin
- `line` _int_ - Overall line counter
- `infileline` _int_ - Line counter in the particular file
- `rawtext` _str_ - Raw input string (except inline code blocks)
- `realraw` _str_ - Unprocessed input
- `name` _str_ - Variable name
- `value` _str_ - Variable value
- `operator` _str_ - Operation performed to the variable
- `flag` _str_ - Optional variable flag

<a id="oelint_parser.cls_item.Variable.VarName"></a>

#### VarName

```python
@property
def VarName()
```

Variable name

**Returns**:

- `str` - name of variable

<a id="oelint_parser.cls_item.Variable.SubItem"></a>

#### SubItem

```python
@property
def SubItem()
```

Variable modifiers

**Returns**:

- `str` - variable modifiers like packages, machines, appends, prepends

<a id="oelint_parser.cls_item.Variable.SubItems"></a>

#### SubItems

```python
@property
def SubItems()
```

Variable modifiers list

**Returns**:

- `list` - variable modifiers list like packages, machines, appends, prepends

<a id="oelint_parser.cls_item.Variable.VarValue"></a>

#### VarValue

```python
@property
def VarValue()
```

variable value

**Returns**:

- `str` - unstripped variable value

<a id="oelint_parser.cls_item.Variable.VarOp"></a>

#### VarOp

```python
@property
def VarOp()
```

Variable operation

**Returns**:

- `str` - operation did on the variable

<a id="oelint_parser.cls_item.Variable.Flag"></a>

#### Flag

```python
@property
def Flag()
```

Variable flag like PACKAGECONFIG[xyz]

**Returns**:

- `str` - variable sub flags

<a id="oelint_parser.cls_item.Variable.VarNameComplete"></a>

#### VarNameComplete

```python
@property
def VarNameComplete()
```

Complete variable name included overrides and flags

**Returns**:

- `str` - complete variable name

<a id="oelint_parser.cls_item.Variable.RawVarName"></a>

#### RawVarName

```python
@property
def RawVarName()
```

Variable name and flags combined

**Returns**:

- `str` - raw representation of the variable name

<a id="oelint_parser.cls_item.Variable.VarValueStripped"></a>

#### VarValueStripped

```python
@property
def VarValueStripped()
```

Stripped variable value

**Returns**:

- `str` - stripped version of variable value

<a id="oelint_parser.cls_item.Variable.IsAppend"></a>

#### IsAppend

```python
def IsAppend()
```

Check if operation is an append

**Returns**:

- `bool` - True is variable is appended

<a id="oelint_parser.cls_item.Variable.AppendOperation"></a>

#### AppendOperation

```python
def AppendOperation()
```

Get variable modifiers

**Returns**:

- `list` - list could contain any combination of 'append', ' += ', 'prepend' and 'remove'

<a id="oelint_parser.cls_item.Variable.get_items"></a>

#### get\_items

```python
def get_items(override="", versioned=False)
```

Get items of variable value

**Arguments**:

- `override` _str_ - String to take instead of VarValue
- `versioned` _bool_ - items can be versioned (versions will be stripped in this case)
  

**Returns**:

- `list` - clean list of items in variable value

<a id="oelint_parser.cls_item.Variable.IsMultiLine"></a>

#### IsMultiLine

```python
def IsMultiLine()
```

Check if variable has a multiline assignment

**Returns**:

- `bool` - True if multiline

<a id="oelint_parser.cls_item.Variable.GetDistroEntry"></a>

#### GetDistroEntry

```python
def GetDistroEntry()
```

Get distro specific entries in variable

**Returns**:

- `str` - distro specific modifier of variable or ""

<a id="oelint_parser.cls_item.Variable.GetMachineEntry"></a>

#### GetMachineEntry

```python
def GetMachineEntry()
```

Get machine specific entries in variable

**Returns**:

- `str` - machine specific modifier of variable or ""

<a id="oelint_parser.cls_item.Variable.GetClassOverride"></a>

#### GetClassOverride

```python
def GetClassOverride()
```

Get class specific entries in variable

**Returns**:

- `str` - class specific modifier of variable or ""

<a id="oelint_parser.cls_item.Comment"></a>

## Comment Objects

```python
class Comment(Item)
```

<a id="oelint_parser.cls_item.Comment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(origin, line, infileline, rawtext, realraw)
```

constructor

**Arguments**:

- `origin` _str_ - Full path to file of origin
- `line` _int_ - Overall line counter
- `infileline` _int_ - Line counter in the particular file
- `rawtext` _str_ - Raw input string (except inline code blocks)
- `realraw` _str_ - Unprocessed input

<a id="oelint_parser.cls_item.Comment.get_items"></a>

#### get\_items

```python
def get_items()
```

Get single lines of block

**Returns**:

- `list` - single lines of comment block

<a id="oelint_parser.cls_item.Include"></a>

## Include Objects

```python
class Include(Item)
```

<a id="oelint_parser.cls_item.Include.__init__"></a>

#### \_\_init\_\_

```python
def __init__(origin, line, infileline, rawtext, incname, statement, realraw)
```

constructor

**Arguments**:

- `origin` _str_ - Full path to file of origin
- `line` _int_ - Overall line counter
- `infileline` _int_ - Line counter in the particular file
- `rawtext` _str_ - Raw input string (except inline code blocks)
- `realraw` _str_ - Unprocessed input
- `incname` _str_ - raw name of the include file
- `statement` _str_ - either include or require

<a id="oelint_parser.cls_item.Include.IncName"></a>

#### IncName

```python
@property
def IncName()
```

Include name

**Returns**:

- `str` - name of the file to include/require

<a id="oelint_parser.cls_item.Include.Statement"></a>

#### Statement

```python
@property
def Statement()
```

statement either include or require

**Returns**:

- `str` - include or require

<a id="oelint_parser.cls_item.Include.get_items"></a>

#### get\_items

```python
def get_items()
```

Get items

**Returns**:

- `list` - include name, include statement

<a id="oelint_parser.cls_item.Export"></a>

## Export Objects

```python
class Export(Item)
```

<a id="oelint_parser.cls_item.Export.__init__"></a>

#### \_\_init\_\_

```python
def __init__(origin, line, infileline, rawtext, name, value, realraw)
```

constructor

**Arguments**:

- `origin` _str_ - Full path to file of origin
- `line` _int_ - Overall line counter
- `infileline` _int_ - Line counter in the particular file
- `rawtext` _str_ - Raw input string (except inline code blocks)
- `realraw` _str_ - Unprocessed input
- `name` _str_ - variable name of the export
- `value` _str_ - (optional) value of the export

<a id="oelint_parser.cls_item.Export.Name"></a>

#### Name

```python
@property
def Name()
```

Name of the exported var

**Returns**:

- `str` - name of the exported var

<a id="oelint_parser.cls_item.Export.Value"></a>

#### Value

```python
@property
def Value()
```

value of the export

**Returns**:

- `str` - optional value of the export

<a id="oelint_parser.cls_item.Export.get_items"></a>

#### get\_items

```python
def get_items()
```

Get items

**Returns**:

- `list` - include name, include statement

<a id="oelint_parser.cls_item.Function"></a>

## Function Objects

```python
class Function(Item)
```

<a id="oelint_parser.cls_item.Function.__init__"></a>

#### \_\_init\_\_

```python
def __init__(origin,
             line,
             infileline,
             rawtext,
             name,
             body,
             realraw,
             python=False,
             fakeroot=False)
```

[summary]

**Arguments**:

- `origin` _str_ - Full path to file of origin
- `line` _int_ - Overall line counter
- `infileline` _int_ - Line counter in the particular file
- `rawtext` _str_ - Raw input string (except inline code blocks)
- `realraw` _str_ - Unprocessed input
- `name` _str_ - Raw function name
- `body` _str_ - Function body
  

**Arguments**:

- `python` _bool_ - python function according to parser (default: {False})
- `fakeroot` _bool_ - uses fakeroot (default: {False})

<a id="oelint_parser.cls_item.Function.IsPython"></a>

#### IsPython

```python
@property
def IsPython()
```

Is python function

**Returns**:

- `bool` - is a python function

<a id="oelint_parser.cls_item.Function.IsFakeroot"></a>

#### IsFakeroot

```python
@property
def IsFakeroot()
```

Is fakeroot function

**Returns**:

- `bool` - is a python function

<a id="oelint_parser.cls_item.Function.FuncName"></a>

#### FuncName

```python
@property
def FuncName()
```

Function name

**Returns**:

- `str` - name of function

<a id="oelint_parser.cls_item.Function.FuncNameComplete"></a>

#### FuncNameComplete

```python
@property
def FuncNameComplete()
```

Complete function name (including overrides)

**Returns**:

- `str` - complete name of function

<a id="oelint_parser.cls_item.Function.SubItem"></a>

#### SubItem

```python
@property
def SubItem()
```

Function modifiers

**Returns**:

- `str` - function modifiers like packages, machines, appends, prepends

<a id="oelint_parser.cls_item.Function.SubItems"></a>

#### SubItems

```python
@property
def SubItems()
```

Function modifiers list

**Returns**:

- `list` - function modifiers list like packages, machines, appends, prepends

<a id="oelint_parser.cls_item.Function.FuncBody"></a>

#### FuncBody

```python
@property
def FuncBody()
```

Function body

**Returns**:

- `str` - function body text

<a id="oelint_parser.cls_item.Function.FuncBodyStripped"></a>

#### FuncBodyStripped

```python
@property
def FuncBodyStripped()
```

Stripped function body

**Returns**:

- `str` - stripped function body text

<a id="oelint_parser.cls_item.Function.FuncBodyRaw"></a>

#### FuncBodyRaw

```python
@property
def FuncBodyRaw()
```

Raw function body (including brackets)

**Returns**:

- `str` - raw function body text

<a id="oelint_parser.cls_item.Function.GetDistroEntry"></a>

#### GetDistroEntry

```python
def GetDistroEntry()
```

Get distro specific modifiers

**Returns**:

- `str` - distro specific modifier or ""

<a id="oelint_parser.cls_item.Function.GetMachineEntry"></a>

#### GetMachineEntry

```python
def GetMachineEntry()
```

Get machine specific modifiers

**Returns**:

- `str` - machine specific modifier or ""

<a id="oelint_parser.cls_item.Function.IsAppend"></a>

#### IsAppend

```python
def IsAppend()
```

Return if function appends another function

**Returns**:

- `bool` - True is append or prepend operation

<a id="oelint_parser.cls_item.Function.get_items"></a>

#### get\_items

```python
def get_items()
```

Get items of function body

**Returns**:

- `list` - single lines of function body

<a id="oelint_parser.cls_item.PythonBlock"></a>

## PythonBlock Objects

```python
class PythonBlock(Item)
```

<a id="oelint_parser.cls_item.PythonBlock.__init__"></a>

#### \_\_init\_\_

```python
def __init__(origin, line, infileline, rawtext, name, realraw)
```

constructor

**Arguments**:

- `origin` _str_ - Full path to file of origin
- `line` _int_ - Overall line counter
- `infileline` _int_ - Line counter in the particular file
- `rawtext` _str_ - Raw input string (except inline code blocks)
- `realraw` _str_ - Unprocessed input
- `name` _str_ - Function name

<a id="oelint_parser.cls_item.PythonBlock.FuncName"></a>

#### FuncName

```python
@property
def FuncName()
```

Function name

**Returns**:

- `str` - name of function

<a id="oelint_parser.cls_item.PythonBlock.get_items"></a>

#### get\_items

```python
def get_items()
```

Get lines of function body

**Returns**:

- `list` - lines of function body

<a id="oelint_parser.cls_item.TaskAssignment"></a>

## TaskAssignment Objects

```python
class TaskAssignment(Item)
```

<a id="oelint_parser.cls_item.TaskAssignment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(origin, line, infileline, rawtext, name, ident, value, realraw)
```

constructor

**Arguments**:

- `origin` _str_ - Full path to file of origin
- `line` _int_ - Overall line counter
- `infileline` _int_ - Line counter in the particular file
- `rawtext` _str_ - Raw input string (except inline code blocks)
- `realraw` _str_ - Unprocessed input
- `name` _str_ - name of task to be modified
- `ident` _str_ - task flag
- `value` _str_ - value of modification

<a id="oelint_parser.cls_item.TaskAssignment.FuncName"></a>

#### FuncName

```python
@property
def FuncName()
```

Function name

**Returns**:

- `str` - name of function

<a id="oelint_parser.cls_item.TaskAssignment.VarValue"></a>

#### VarValue

```python
@property
def VarValue()
```

Task flag value

**Returns**:

- `str` - Task flag value

<a id="oelint_parser.cls_item.TaskAssignment.VarName"></a>

#### VarName

```python
@property
def VarName()
```

Task flag name

**Returns**:

- `str` - name of task flag

<a id="oelint_parser.cls_item.TaskAssignment.get_items"></a>

#### get\_items

```python
def get_items()
```

Get items

**Returns**:

- `list` - function name, flag, modification value

<a id="oelint_parser.cls_item.FunctionExports"></a>

## FunctionExports Objects

```python
class FunctionExports(Item)
```

<a id="oelint_parser.cls_item.FunctionExports.__init__"></a>

#### \_\_init\_\_

```python
def __init__(origin, line, infileline, rawtext, name, realraw)
```

constructor

**Arguments**:

- `origin` _str_ - Full path to file of origin
- `line` _int_ - Overall line counter
- `infileline` _int_ - Line counter in the particular file
- `rawtext` _str_ - Raw input string (except inline code blocks)
- `realraw` _str_ - Unprocessed input
- `name` _str_ - name of function to be exported

<a id="oelint_parser.cls_item.FunctionExports.FuncNames"></a>

#### FuncNames

```python
@property
def FuncNames()
```

Function name

**Returns**:

- `str` - names of exported functions

<a id="oelint_parser.cls_item.FunctionExports.get_items"></a>

#### get\_items

```python
def get_items()
```

Get items

**Returns**:

- `list` - function names

<a id="oelint_parser.cls_item.FunctionExports.get_items_unaliased"></a>

#### get\_items\_unaliased

```python
def get_items_unaliased()
```

Get items with their bbclass scope names

**Returns**:

- `list` - function names in the scope of a bbclass (foo becomes classname-foo in this case)

<a id="oelint_parser.cls_item.TaskAdd"></a>

## TaskAdd Objects

```python
class TaskAdd(Item)
```

<a id="oelint_parser.cls_item.TaskAdd.__init__"></a>

#### \_\_init\_\_

```python
def __init__(origin,
             line,
             infileline,
             rawtext,
             name,
             realraw,
             before="",
             after="")
```

constructor

**Arguments**:

- `origin` _str_ - Full path to file of origin
- `line` _int_ - Overall line counter
- `infileline` _int_ - Line counter in the particular file
- `rawtext` _str_ - Raw input string (except inline code blocks)
- `realraw` _str_ - Unprocessed input
- `name` _str_ - name of task to be executed
  

**Arguments**:

- `before` _str_ - before statement (default: {""})
- `after` _str_ - after statement (default: {""})

<a id="oelint_parser.cls_item.TaskAdd.FuncName"></a>

#### FuncName

```python
@property
def FuncName()
```

Function name

**Returns**:

- `str` - name of function

<a id="oelint_parser.cls_item.TaskAdd.Before"></a>

#### Before

```python
@property
def Before()
```

Tasks executed before

**Returns**:

- `list` - tasks to be executed before

<a id="oelint_parser.cls_item.TaskAdd.After"></a>

#### After

```python
@property
def After()
```

Tasks executed after

**Returns**:

- `list` - tasks to be executed after

<a id="oelint_parser.cls_item.TaskAdd.get_items"></a>

#### get\_items

```python
def get_items()
```

get items

**Returns**:

- `list` - function name, all before statements, all after statements

<a id="oelint_parser.cls_item.MissingFile"></a>

## MissingFile Objects

```python
class MissingFile(Item)
```

<a id="oelint_parser.cls_item.MissingFile.__init__"></a>

#### \_\_init\_\_

```python
def __init__(origin, line, infileline, filename, statement)
```

constructor

**Arguments**:

- `origin` _str_ - Full path to file of origin
- `line` _int_ - Overall line counter
- `infileline` _int_ - Line counter in the particular file
- `filename` _str_ - filename of the file that can't be found
- `statement` _str_ - either include or require

<a id="oelint_parser.cls_item.MissingFile.Filename"></a>

#### Filename

```python
@property
def Filename()
```

Filename of the file missing

**Returns**:

- `str` - filename that can't be resolved

<a id="oelint_parser.cls_item.MissingFile.Statement"></a>

#### Statement

```python
@property
def Statement()
```

statement either include or require

**Returns**:

- `str` - include or require

<a id="oelint_parser.parser"></a>

# oelint\_parser.parser

<a id="oelint_parser.parser.get_full_scope"></a>

#### get\_full\_scope

```python
def get_full_scope(_string, offset, _sstart, _send)
```

get full block of an inline statement

**Arguments**:

- `_string` _str_ - input string
- `offset` _int_ - offset in string
- `_sstart` _int_ - block start index
- `_send` _int_ - block end index
  

**Returns**:

- `str` - full block on inline statement

<a id="oelint_parser.parser.prepare_lines_subparser"></a>

#### prepare\_lines\_subparser

```python
def prepare_lines_subparser(_iter, lineOffset, num, line, raw_line=None)
```

preprocess raw input

**Arguments**:

- `_iter` _interator_ - line interator object
- `lineOffset` _int_ - current line index
- `num` _int_ - internal line counter
- `line` _int_ - input string
- `raw_line` _string, optional_ - internal line representation. Defaults to None.
  

**Returns**:

- `list` - list of preproccessed chunks

<a id="oelint_parser.parser.prepare_lines"></a>

#### prepare\_lines

```python
def prepare_lines(_file, lineOffset=0)
```

break raw file input into preprocessed chunks

**Arguments**:

- `_file` _string_ - Full path to file
- `lineOffset` _int, optional_ - line offset counter. Defaults to 0.
  

**Returns**:

- `list` - preprocessed list of chunks

<a id="oelint_parser.parser.get_items"></a>

#### get\_items

```python
def get_items(stash, _file, lineOffset=0)
```

parses file

**Arguments**:

- `stash` _oelint_parser.cls_stash.Stash_ - Stash object
- `_file` _string_ - Full path to file
- `lineOffset` _int, optional_ - line offset counter. Defaults to 0.
  

**Returns**:

- `list` - List of oelint_parser.cls_item.* representations

