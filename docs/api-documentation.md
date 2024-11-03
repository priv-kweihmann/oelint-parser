# Table of Contents

* [oelint\_parser](#oelint_parser)
* [oelint\_parser.cls\_stash](#oelint_parser.cls_stash)
  * [Stash](#oelint_parser.cls_stash.Stash)
    * [StashList](#oelint_parser.cls_stash.Stash.StashList)
    * [\_\_init\_\_](#oelint_parser.cls_stash.Stash.__init__)
    * [AddFile](#oelint_parser.cls_stash.Stash.AddFile)
    * [FingerPrint](#oelint_parser.cls_stash.Stash.FingerPrint)
    * [Append](#oelint_parser.cls_stash.Stash.Append)
    * [Remove](#oelint_parser.cls_stash.Stash.Remove)
    * [AddDistroMachineFromLayer](#oelint_parser.cls_stash.Stash.AddDistroMachineFromLayer)
    * [Finalize](#oelint_parser.cls_stash.Stash.Finalize)
    * [GetRecipes](#oelint_parser.cls_stash.Stash.GetRecipes)
    * [GetLoneAppends](#oelint_parser.cls_stash.Stash.GetLoneAppends)
    * [GetConfFiles](#oelint_parser.cls_stash.Stash.GetConfFiles)
    * [GetLinksForFile](#oelint_parser.cls_stash.Stash.GetLinksForFile)
    * [Reduce](#oelint_parser.cls_stash.Stash.Reduce)
    * [GetItemsFor](#oelint_parser.cls_stash.Stash.GetItemsFor)
    * [ExpandVar](#oelint_parser.cls_stash.Stash.ExpandVar)
    * [GetFiles](#oelint_parser.cls_stash.Stash.GetFiles)
    * [GetLayerRoot](#oelint_parser.cls_stash.Stash.GetLayerRoot)
    * [FindLocalOrLayer](#oelint_parser.cls_stash.Stash.FindLocalOrLayer)
    * [GetScrComponents](#oelint_parser.cls_stash.Stash.GetScrComponents)
    * [SafeLineSplit](#oelint_parser.cls_stash.Stash.SafeLineSplit)
    * [GuessRecipeName](#oelint_parser.cls_stash.Stash.GuessRecipeName)
    * [GuessBaseRecipeName](#oelint_parser.cls_stash.Stash.GuessBaseRecipeName)
    * [GuessRecipeVersion](#oelint_parser.cls_stash.Stash.GuessRecipeVersion)
    * [ExpandTerm](#oelint_parser.cls_stash.Stash.ExpandTerm)
    * [GetValidPackageNames](#oelint_parser.cls_stash.Stash.GetValidPackageNames)
    * [GetValidNamedResources](#oelint_parser.cls_stash.Stash.GetValidNamedResources)
    * [IsImage](#oelint_parser.cls_stash.Stash.IsImage)
    * [IsPackageGroup](#oelint_parser.cls_stash.Stash.IsPackageGroup)
* [oelint\_parser.rpl\_regex](#oelint_parser.rpl_regex)
  * [RegexRpl](#oelint_parser.rpl_regex.RegexRpl)
    * [search](#oelint_parser.rpl_regex.RegexRpl.search)
    * [split](#oelint_parser.rpl_regex.RegexRpl.split)
    * [match](#oelint_parser.rpl_regex.RegexRpl.match)
    * [sub](#oelint_parser.rpl_regex.RegexRpl.sub)
    * [finditer](#oelint_parser.rpl_regex.RegexRpl.finditer)
* [oelint\_parser.inlinerep](#oelint_parser.inlinerep)
  * [bb\_utils\_filter](#oelint_parser.inlinerep.bb_utils_filter)
  * [bb\_utils\_contains](#oelint_parser.inlinerep.bb_utils_contains)
  * [bb\_utils\_contains\_any](#oelint_parser.inlinerep.bb_utils_contains_any)
  * [oe\_utils\_conditional](#oelint_parser.inlinerep.oe_utils_conditional)
  * [oe\_utils\_ifelse](#oelint_parser.inlinerep.oe_utils_ifelse)
  * [oe\_utils\_any\_distro\_features](#oelint_parser.inlinerep.oe_utils_any_distro_features)
  * [oe\_utils\_all\_distro\_features](#oelint_parser.inlinerep.oe_utils_all_distro_features)
  * [oe\_utils\_vartrue](#oelint_parser.inlinerep.oe_utils_vartrue)
  * [oe\_utils\_less\_or\_equal](#oelint_parser.inlinerep.oe_utils_less_or_equal)
  * [oe\_utils\_version\_less\_or\_equal](#oelint_parser.inlinerep.oe_utils_version_less_or_equal)
  * [oe\_utils\_both\_contain](#oelint_parser.inlinerep.oe_utils_both_contain)
  * [inlinerep](#oelint_parser.inlinerep.inlinerep)
* [oelint\_parser.constants](#oelint_parser.constants)
  * [Constants](#oelint_parser.constants.Constants)
    * [GetByPath](#oelint_parser.constants.Constants.GetByPath)
    * [AddConstants](#oelint_parser.constants.Constants.AddConstants)
    * [RemoveConstants](#oelint_parser.constants.Constants.RemoveConstants)
    * [OverrideConstants](#oelint_parser.constants.Constants.OverrideConstants)
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
  * [\_\_id\_regex\_\_](#oelint_parser.cls_item.__id_regex__)
  * [Item](#oelint_parser.cls_item.Item)
    * [\_\_init\_\_](#oelint_parser.cls_item.Item.__init__)
    * [Line](#oelint_parser.cls_item.Item.Line)
    * [Raw](#oelint_parser.cls_item.Item.Raw)
    * [Origin](#oelint_parser.cls_item.Item.Origin)
    * [InFileLine](#oelint_parser.cls_item.Item.InFileLine)
    * [RealRaw](#oelint_parser.cls_item.Item.RealRaw)
    * [IsFromClass](#oelint_parser.cls_item.Item.IsFromClass)
    * [OverrideDelimiter](#oelint_parser.cls_item.Item.OverrideDelimiter)
    * [IsNewStyleOverrideSyntax](#oelint_parser.cls_item.Item.IsNewStyleOverrideSyntax)
    * [safe\_linesplit](#oelint_parser.cls_item.Item.safe_linesplit)
    * [get\_items](#oelint_parser.cls_item.Item.get_items)
    * [extract\_sub](#oelint_parser.cls_item.Item.extract_sub)
    * [extract\_sub\_func](#oelint_parser.cls_item.Item.extract_sub_func)
    * [IsFromAppend](#oelint_parser.cls_item.Item.IsFromAppend)
    * [GetAttributes](#oelint_parser.cls_item.Item.GetAttributes)
  * [Variable](#oelint_parser.cls_item.Variable)
    * [\_\_init\_\_](#oelint_parser.cls_item.Variable.__init__)
    * [VarName](#oelint_parser.cls_item.Variable.VarName)
    * [SubItem](#oelint_parser.cls_item.Variable.SubItem)
    * [SubItems](#oelint_parser.cls_item.Variable.SubItems)
    * [VarValue](#oelint_parser.cls_item.Variable.VarValue)
    * [VarOp](#oelint_parser.cls_item.Variable.VarOp)
    * [VarNameComplete](#oelint_parser.cls_item.Variable.VarNameComplete)
    * [VarNameCompleteNoModifiers](#oelint_parser.cls_item.Variable.VarNameCompleteNoModifiers)
    * [RawVarName](#oelint_parser.cls_item.Variable.RawVarName)
    * [VarValueStripped](#oelint_parser.cls_item.Variable.VarValueStripped)
    * [IsAppend](#oelint_parser.cls_item.Variable.IsAppend)
    * [AppendOperation](#oelint_parser.cls_item.Variable.AppendOperation)
    * [get\_items](#oelint_parser.cls_item.Variable.get_items)
    * [IsMultiLine](#oelint_parser.cls_item.Variable.IsMultiLine)
    * [GetDistroEntry](#oelint_parser.cls_item.Variable.GetDistroEntry)
    * [GetMachineEntry](#oelint_parser.cls_item.Variable.GetMachineEntry)
    * [GetClassOverride](#oelint_parser.cls_item.Variable.GetClassOverride)
    * [IsImmediateModify](#oelint_parser.cls_item.Variable.IsImmediateModify)
  * [Comment](#oelint_parser.cls_item.Comment)
    * [\_\_init\_\_](#oelint_parser.cls_item.Comment.__init__)
    * [get\_items](#oelint_parser.cls_item.Comment.get_items)
  * [Include](#oelint_parser.cls_item.Include)
    * [\_\_init\_\_](#oelint_parser.cls_item.Include.__init__)
    * [IncName](#oelint_parser.cls_item.Include.IncName)
    * [Statement](#oelint_parser.cls_item.Include.Statement)
    * [FileIncluded](#oelint_parser.cls_item.Include.FileIncluded)
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
  * [FlagAssignment](#oelint_parser.cls_item.FlagAssignment)
    * [\_\_init\_\_](#oelint_parser.cls_item.FlagAssignment.__init__)
    * [VarName](#oelint_parser.cls_item.FlagAssignment.VarName)
    * [Flag](#oelint_parser.cls_item.FlagAssignment.Flag)
    * [VarOp](#oelint_parser.cls_item.FlagAssignment.VarOp)
    * [Value](#oelint_parser.cls_item.FlagAssignment.Value)
    * [ValueStripped](#oelint_parser.cls_item.FlagAssignment.ValueStripped)
    * [get\_items](#oelint_parser.cls_item.FlagAssignment.get_items)
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
    * [Comment](#oelint_parser.cls_item.TaskAdd.Comment)
    * [get\_items](#oelint_parser.cls_item.TaskAdd.get_items)
  * [TaskDel](#oelint_parser.cls_item.TaskDel)
    * [\_\_init\_\_](#oelint_parser.cls_item.TaskDel.__init__)
    * [FuncName](#oelint_parser.cls_item.TaskDel.FuncName)
    * [Comment](#oelint_parser.cls_item.TaskDel.Comment)
    * [get\_items](#oelint_parser.cls_item.TaskDel.get_items)
  * [MissingFile](#oelint_parser.cls_item.MissingFile)
    * [\_\_init\_\_](#oelint_parser.cls_item.MissingFile.__init__)
    * [Filename](#oelint_parser.cls_item.MissingFile.Filename)
    * [Statement](#oelint_parser.cls_item.MissingFile.Statement)
  * [AddPylib](#oelint_parser.cls_item.AddPylib)
    * [\_\_init\_\_](#oelint_parser.cls_item.AddPylib.__init__)
    * [Path](#oelint_parser.cls_item.AddPylib.Path)
    * [Namespace](#oelint_parser.cls_item.AddPylib.Namespace)
    * [get\_items](#oelint_parser.cls_item.AddPylib.get_items)
  * [Inherit](#oelint_parser.cls_item.Inherit)
    * [\_\_init\_\_](#oelint_parser.cls_item.Inherit.__init__)
    * [Class](#oelint_parser.cls_item.Inherit.Class)
    * [Statement](#oelint_parser.cls_item.Inherit.Statement)
    * [FilePaths](#oelint_parser.cls_item.Inherit.FilePaths)
    * [get\_items](#oelint_parser.cls_item.Inherit.get_items)
  * [Unset](#oelint_parser.cls_item.Unset)
    * [\_\_init\_\_](#oelint_parser.cls_item.Unset.__init__)
    * [VarName](#oelint_parser.cls_item.Unset.VarName)
    * [Flag](#oelint_parser.cls_item.Unset.Flag)
    * [get\_items](#oelint_parser.cls_item.Unset.get_items)
* [oelint\_parser.parser](#oelint_parser.parser)
  * [get\_full\_scope](#oelint_parser.parser.get_full_scope)
  * [prepare\_lines\_subparser](#oelint_parser.parser.prepare_lines_subparser)
  * [prepare\_lines](#oelint_parser.parser.prepare_lines)
  * [get\_items](#oelint_parser.parser.get_items)

<a id="oelint_parser"></a>

# oelint\_parser

oelint_parser is a library to parse bitbake files.

<a id="oelint_parser.cls_stash"></a>

# oelint\_parser.cls\_stash

<a id="oelint_parser.cls_stash.Stash"></a>

## Stash Objects

```python
class Stash()
```

The Stash object is the central storage for extracting the bitbake information.

<a id="oelint_parser.cls_stash.Stash.StashList"></a>

## StashList Objects

```python
class StashList(UserList)
```

Extended list of Items.

<a id="oelint_parser.cls_stash.Stash.StashList.__init__"></a>

#### \_\_init\_\_

```python
def __init__(stash: 'Stash', items: Iterable[Item]) -> None
```

StashList - Extended list of Items.

**Arguments**:

- `stash` _Stash_ - Parent stash object
- `items` _Iterable_ - Iterable input

<a id="oelint_parser.cls_stash.Stash.StashList.insert"></a>

#### insert

```python
def insert(index: int, item: Item) -> None
```

Insert into list

**Arguments**:

- `index` _int_ - index where to insert
- `item` _Item_ - object to insert

<a id="oelint_parser.cls_stash.Stash.StashList.append"></a>

#### append

```python
def append(item: Union[Item, Iterable[Item]]) -> None
```

Append to list

**Arguments**:

- `item` _Union[Item, Iterable[Item]]_ - Item or Iterable of Items

<a id="oelint_parser.cls_stash.Stash.StashList.extend"></a>

#### extend

```python
def extend(other: 'Stash.StashList') -> None
```

Extend list

**Arguments**:

- `other` _Stash.StashList_ - Other stash other

<a id="oelint_parser.cls_stash.Stash.StashList.remove"></a>

#### remove

```python
def remove(item: Union[Item, Iterable[Item]]) -> None
```

Remove from list

**Arguments**:

- `item` _Item_ - Item(s) to remove

<a id="oelint_parser.cls_stash.Stash.StashList.reduce"></a>

#### reduce

```python
def reduce(filename: str = None,
           classifier: Union[Iterable[str], str] = None,
           attribute: Union[Iterable[str], str] = None,
           attributeValue: Union[Iterable[str], str] = None,
           nolink: bool = False) -> 'Stash.StashList'
```

Filters the list.

NOTE: This is a destructive operation.
If you want to have a copy returned use

Stash.Reduce(<this object>,...) instead.

**Arguments**:

- `filename` _str, optional_ - Full path to file. Defaults to None.
- `classifier` _Union[Iterable[str], str], optional_ - (iterable of) class specifier (e.g. Variable). Defaults to None.
- `attribute` _Union[Iterable[str], str], optional_ - (iterable of) class attribute name. Defaults to None.
- `attributeValue` _Union[Iterable[str], str], optional_ - (iterable of) value of the class attribute value. Defaults to None.
- `nolink` _bool, optional_ - Consider linked files. Defaults to False.
  

**Returns**:

- `Stash.StashList` - self

<a id="oelint_parser.cls_stash.Stash.__init__"></a>

#### \_\_init\_\_

```python
def __init__(quiet: bool = False,
             new_style_override_syntax: bool = False,
             negative_inline: bool = False) -> None
```

Stash object

**Arguments**:

- `quiet` _bool, optional_ - No progress printing. Defaults to False.
- `new_style_override_syntax` _bool, optional_ - Enforce new override syntax. Defaults to False.
- `negative_inline` _bool, optional_ - Negative branch inline expansion. Defaults to False.

<a id="oelint_parser.cls_stash.Stash.AddFile"></a>

#### AddFile

```python
def AddFile(_file: str,
            lineOffset: int = 0,
            forcedLink: str = None) -> List[Item]
```

Adds a file to the stash

**Arguments**:

- `_file` _str_ - Full path to file
  

**Arguments**:

- `lineOffset` _int_ - Line offset from the file that include this file (default: {0})
- `forcedLink` _type_ - Force link against a file (default: {None})
  

**Returns**:

- `list` - List of {oelint_parser.cls_item.Item}

<a id="oelint_parser.cls_stash.Stash.FingerPrint"></a>

#### FingerPrint

```python
@property
def FingerPrint() -> str
```

Get the SHA1 fingerprint of the current Stash

**Returns**:

- `str` - hexdigest checksum

<a id="oelint_parser.cls_stash.Stash.Append"></a>

#### Append

```python
def Append(item: Union[Item, Iterable[Item]]) -> None
```

appends one or mote items to the stash

**Arguments**:

- `item` _Item_ - Item(s) to append

<a id="oelint_parser.cls_stash.Stash.Remove"></a>

#### Remove

```python
def Remove(item: Union[Item, Iterable[Item]]) -> None
```

removes one or more items from the stash

**Arguments**:

- `item` _Item_ - Item(s) to remove

<a id="oelint_parser.cls_stash.Stash.AddDistroMachineFromLayer"></a>

#### AddDistroMachineFromLayer

```python
def AddDistroMachineFromLayer(path: str) -> None
```

adds machine and distro configuration from the layer of the provided file

**Arguments**:

- `path` _str_ - Path to file

<a id="oelint_parser.cls_stash.Stash.Finalize"></a>

#### Finalize

```python
def Finalize() -> None
```

finalize the dependencies within the stash

<a id="oelint_parser.cls_stash.Stash.GetRecipes"></a>

#### GetRecipes

```python
@functools.cache
def GetRecipes() -> None
```

Get bb files in stash

**Returns**:

- `list` - List of bb files in stash

<a id="oelint_parser.cls_stash.Stash.GetLoneAppends"></a>

#### GetLoneAppends

```python
@functools.cache
def GetLoneAppends() -> List[str]
```

Get bbappend without a matching bb

**Returns**:

- `list` - list of bbappend without a matching bb

<a id="oelint_parser.cls_stash.Stash.GetConfFiles"></a>

#### GetConfFiles

```python
@functools.cache
def GetConfFiles() -> List[str]
```

Get configurations files

**Returns**:

- `List[str]` - List of configuration files

<a id="oelint_parser.cls_stash.Stash.GetLinksForFile"></a>

#### GetLinksForFile

```python
@functools.cache
def GetLinksForFile(filename: str) -> List[str]
```

Get file which this file is linked against

**Arguments**:

- `filename` _str_ - full path to file
  

**Returns**:

- `list` - list of full paths the file is linked against

<a id="oelint_parser.cls_stash.Stash.Reduce"></a>

#### Reduce

```python
def Reduce(in_list: Iterable[Item],
           filename: str = None,
           classifier: Union[Iterable[str], str] = None,
           attribute: Union[Iterable[str], str] = None,
           attributeValue: Union[Iterable[str], str] = None,
           nolink: bool = False) -> List[Item]
```

Reduce a list by filtering

**Arguments**:

- `in_list` _Stash.StashList_ - Input list.
- `filename` _str, optional_ - Full path to file. Defaults to None.
- `classifier` _Union[Iterable[str], str], optional_ - (iterable of) class specifier (e.g. Variable). Defaults to None.
- `attribute` _Union[Iterable[str], str], optional_ - (iterable of) class attribute name. Defaults to None.
- `attributeValue` _Union[Iterable[str], str], optional_ - (iterable of) value of the class attribute value. Defaults to None.
- `nolink` _bool, optional_ - Consider linked files. Defaults to False.
  

**Returns**:

- `List[Item]` - Returns a list of items fitting the set filters

<a id="oelint_parser.cls_stash.Stash.GetItemsFor"></a>

#### GetItemsFor

```python
def GetItemsFor(filename: str = None,
                classifier: Union[Iterable[str], str] = None,
                attribute: Union[Iterable[str], str] = None,
                attributeValue: Union[Iterable[str], str] = None,
                nolink: bool = False) -> 'Stash.StashList'
```

Get items for filename

**Arguments**:

- `filename` _str, optional_ - Full path to file. Defaults to None.
- `classifier` _Union[Iterable[str], str], optional_ - (iterable of) class specifier (e.g. Variable). Defaults to None.
- `attribute` _Union[Iterable[str], str], optional_ - (iterable of) class attribute name. Defaults to None.
- `attributeValue` _Union[Iterable[str], str], optional_ - (iterable of) value of the class attribute value. Defaults to None.
- `nolink` _bool, optional_ - Consider linked files. Defaults to False.
  

**Returns**:

- `Stash.StashList` - Returns a list of items fitting the set filters

<a id="oelint_parser.cls_stash.Stash.ExpandVar"></a>

#### ExpandVar

```python
def ExpandVar(filename: str = None,
              attribute: Union[Iterable[str], str] = None,
              attributeValue: Union[Iterable[str], str] = None,
              nolink: bool = False) -> dict
```

Expand variable to dictionary

**Arguments**:

- `filename` _str_ - Full path to file (default: {None})
- `attribute` _str_ - class attribute name (default: {None})
- `attributeValue` _str_ - value of the class attribute name (default: {None})
- `nolink` _bool_ - Consider linked files (default: {False})
  

**Returns**:

- `{dict}` - expanded variables from call + base set of variables

<a id="oelint_parser.cls_stash.Stash.GetFiles"></a>

#### GetFiles

```python
@functools.cache
def GetFiles(_file: str, pattern: str) -> List[str]
```

Get files matching SRC_URI entries

**Arguments**:

- `_file` _str_ - Full path to filename
- `pattern` _str_ - glob pattern to apply
  

**Returns**:

- `list` - list of files matching pattern

<a id="oelint_parser.cls_stash.Stash.GetLayerRoot"></a>

#### GetLayerRoot

```python
@functools.cache
def GetLayerRoot(name: str) -> str
```

Find the path to the layer root of a file

**Arguments**:

- `name` _str_ - filename
  

**Returns**:

- `str` - path to layer root or empty string

<a id="oelint_parser.cls_stash.Stash.FindLocalOrLayer"></a>

#### FindLocalOrLayer

```python
@functools.cache
def FindLocalOrLayer(name: str, localdir: str) -> str
```

Find file in local dir or in layer

**Arguments**:

- `name` _str_ - filename
- `localdir` _str_ - path to local dir
  

**Returns**:

- `str` - path to found file or None

<a id="oelint_parser.cls_stash.Stash.GetScrComponents"></a>

#### GetScrComponents

```python
@functools.cache
def GetScrComponents(string: str) -> dict
```

Return SRC_URI components

**Arguments**:

- `string` _str_ - raw string
  

**Returns**:

- `dict` - scheme: protocol used, src: source URI, options: parsed options

<a id="oelint_parser.cls_stash.Stash.SafeLineSplit"></a>

#### SafeLineSplit

```python
@functools.cache
def SafeLineSplit(string: str) -> List[str]
```

Split line in a safe manner

**Arguments**:

- `string` _str_ - raw input
  

**Returns**:

- `list` - safely split input

<a id="oelint_parser.cls_stash.Stash.GuessRecipeName"></a>

#### GuessRecipeName

```python
@functools.cache
def GuessRecipeName(_file: str) -> str
```

Get the recipe name from filename

**Arguments**:

- `_file` _str_ - filename
  

**Returns**:

- `str` - recipe name

<a id="oelint_parser.cls_stash.Stash.GuessBaseRecipeName"></a>

#### GuessBaseRecipeName

```python
@functools.cache
def GuessBaseRecipeName(_file: str) -> str
```

Get the base recipe name from filename (aka BPN)

**Arguments**:

- `_file` _str_ - filename
  

**Returns**:

- `str` - recipe name

<a id="oelint_parser.cls_stash.Stash.GuessRecipeVersion"></a>

#### GuessRecipeVersion

```python
@functools.cache
def GuessRecipeVersion(_file: str) -> str
```

Get recipe version from filename

**Arguments**:

- `_file` _str_ - filename
  

**Returns**:

- `str` - recipe version

<a id="oelint_parser.cls_stash.Stash.ExpandTerm"></a>

#### ExpandTerm

```python
def ExpandTerm(_file: str,
               value: str,
               spare: List[str] = None,
               seen: List[str] = None) -> str
```

Expand a variable (replacing all variables by known content)

**Arguments**:

- `_file` _str_ - Full path to file
- `value` _str_ - Variable value to expand
- `spare` _list[str]_ - items to keep unexpanded (default: None)
- `seen` _list[str]_ - seen items (default: None)
  

**Returns**:

- `str` - expanded value

<a id="oelint_parser.cls_stash.Stash.GetValidPackageNames"></a>

#### GetValidPackageNames

```python
@functools.cache
def GetValidPackageNames(_file: str, strippn: bool = False) -> List[str]
```

Get known valid names for packages

**Arguments**:

- `_file` _str_ - Full path to file
- `strippn` _bool_ - strip the package name (default: False)
  

**Returns**:

- `list` - list of valid package names

<a id="oelint_parser.cls_stash.Stash.GetValidNamedResources"></a>

#### GetValidNamedResources

```python
@functools.cache
def GetValidNamedResources(_file: str) -> List[str]
```

Get list of valid SRCREV resource names

**Arguments**:

- `_file` _str_ - Full path to file
  

**Returns**:

- `list` - list of valid SRCREV resource names

<a id="oelint_parser.cls_stash.Stash.IsImage"></a>

#### IsImage

```python
@functools.cache
def IsImage(_file: str) -> bool
```

returns if the file is likely an image recipe or not

**Arguments**:

- `_file` _str_ - Full path to file
  

**Returns**:

- `bool` - True if _file is an image recipe

<a id="oelint_parser.cls_stash.Stash.IsPackageGroup"></a>

#### IsPackageGroup

```python
@functools.cache
def IsPackageGroup(_file: str) -> bool
```

returns if the file is likely a packagegroup recipe or not

**Arguments**:

- `_file` _str_ - Full path to file
  

**Returns**:

- `bool` - True if _file is a packagegroup recipe

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
def search(pattern: str,
           string: str,
           timeout: int = 5,
           default: object = None,
           **kwargs) -> Union[Match, None]
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
def split(pattern: str,
          string: str,
          timeout: int = 5,
          default: object = None,
          **kwargs) -> List[str]
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
def match(pattern: str,
          string: str,
          timeout: int = 5,
          default: object = None,
          **kwargs) -> Union[Match, None]
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
def sub(pattern: str,
        repl: str,
        string: str,
        timeout: int = 5,
        default: str = '',
        **kwargs) -> str
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
def finditer(pattern: str,
             string: str,
             timeout: int = 5,
             default: object = None,
             **kwargs) -> Scanner
```

replacement for re.finditer

**Arguments**:

- `pattern` _str_ - regex pattern
- `string` _str_ - input string
- `timeout` _int, optional_ - Timeout for operation. On timeout `default` will be returned. Defaults to 5.
- `default` __type_, optional_ - Default to return on timeout. Defaults to None.
  

**Returns**:

- `Scanner` - Scanner object or None

<a id="oelint_parser.inlinerep"></a>

# oelint\_parser.inlinerep

<a id="oelint_parser.inlinerep.bb_utils_filter"></a>

#### bb\_utils\_filter

```python
def bb_utils_filter(_in: str, negative_clause: bool = False) -> str
```

bb.utils.filter emulation

**Arguments**:

- `_in` _str_ - Input string
- `negative_clause` _bool_ - return negative branch
  

**Returns**:

- `str` - True argument of the conditional or None if not applicable

<a id="oelint_parser.inlinerep.bb_utils_contains"></a>

#### bb\_utils\_contains

```python
def bb_utils_contains(_in: str, negative_clause: bool = False) -> str
```

bb.utils.contains emulation

**Arguments**:

- `_in` _str_ - Input string
- `negative_clause` _bool_ - return negative branch
  

**Returns**:

- `str` - True argument of the conditional or None if not applicable

<a id="oelint_parser.inlinerep.bb_utils_contains_any"></a>

#### bb\_utils\_contains\_any

```python
def bb_utils_contains_any(_in: str, negative_clause: bool = False) -> str
```

bb.utils.contains_any emulation

**Arguments**:

- `_in` _str_ - Input string
- `negative_clause` _bool_ - return negative branch
  

**Returns**:

- `str` - True argument of the conditional or None if not applicable

<a id="oelint_parser.inlinerep.oe_utils_conditional"></a>

#### oe\_utils\_conditional

```python
def oe_utils_conditional(_in: str, negative_clause: bool = False) -> str
```

oe.utils.conditional emulation

**Arguments**:

- `_in` _str_ - Input string
- `negative_clause` _bool_ - return negative branch
  

**Returns**:

- `str` - True argument of the conditional or None if not applicable

<a id="oelint_parser.inlinerep.oe_utils_ifelse"></a>

#### oe\_utils\_ifelse

```python
def oe_utils_ifelse(_in: str, negative_clause: bool = False) -> str
```

oe.utils.ifelse emulation

**Arguments**:

- `_in` _str_ - Input string
- `negative_clause` _bool_ - return negative branch
  

**Returns**:

- `str` - True argument of the conditional or None if not applicable

<a id="oelint_parser.inlinerep.oe_utils_any_distro_features"></a>

#### oe\_utils\_any\_distro\_features

```python
def oe_utils_any_distro_features(_in: str,
                                 negative_clause: bool = False) -> str
```

oe.utils.any_distro_features emulation

**Arguments**:

- `_in` _str_ - Input string
- `negative_clause` _bool_ - return negative branch
  

**Returns**:

- `str` - True argument of the conditional or None if not applicable

<a id="oelint_parser.inlinerep.oe_utils_all_distro_features"></a>

#### oe\_utils\_all\_distro\_features

```python
def oe_utils_all_distro_features(_in: str,
                                 negative_clause: bool = False) -> str
```

oe.utils.all_distro_features emulation

**Arguments**:

- `_in` _str_ - Input string
- `negative_clause` _bool_ - return negative branch
  

**Returns**:

- `str` - True argument of the conditional or None if not applicable

<a id="oelint_parser.inlinerep.oe_utils_vartrue"></a>

#### oe\_utils\_vartrue

```python
def oe_utils_vartrue(_in: str, negative_clause: bool = False) -> str
```

oe.utils.vartrue emulation

**Arguments**:

- `_in` _str_ - Input string
- `negative_clause` _bool_ - return negative branch
  

**Returns**:

- `str` - True argument of the conditional or None if not applicable

<a id="oelint_parser.inlinerep.oe_utils_less_or_equal"></a>

#### oe\_utils\_less\_or\_equal

```python
def oe_utils_less_or_equal(_in: str, negative_clause: bool = False) -> str
```

oe.utils.less_or_equal emulation

**Arguments**:

- `_in` _str_ - Input string
- `negative_clause` _bool_ - return negative branch
  

**Returns**:

- `str` - True argument of the conditional or None if not applicable

<a id="oelint_parser.inlinerep.oe_utils_version_less_or_equal"></a>

#### oe\_utils\_version\_less\_or\_equal

```python
def oe_utils_version_less_or_equal(_in: str,
                                   negative_clause: bool = False) -> str
```

oe.utils.version_less_or_equal emulation

**Arguments**:

- `_in` _str_ - Input string
- `negative_clause` _bool_ - return negative branch
  

**Returns**:

- `str` - True argument of the conditional or None if not applicable

<a id="oelint_parser.inlinerep.oe_utils_both_contain"></a>

#### oe\_utils\_both\_contain

```python
def oe_utils_both_contain(_in: str, negative_clause: bool = False) -> str
```

oe.utils.both_contain emulation

**Arguments**:

- `_in` _str_ - Input string
- `negative_clause` _bool_ - return negative branch
  

**Returns**:

- `str` - True argument of the conditional or None if not applicable

<a id="oelint_parser.inlinerep.inlinerep"></a>

#### inlinerep

```python
def inlinerep(_in: str, negative_clause: bool = False) -> str
```

Replaces inline code expressions

**Arguments**:

- `_in` _str_ - Input string
- `negative_clause` _bool_ - return negative branch
  

**Returns**:

- `str` - Expanded string or None, if not applicable

<a id="oelint_parser.constants"></a>

# oelint\_parser.constants

<a id="oelint_parser.constants.Constants"></a>

## Constants Objects

```python
class Constants()
```

Interface for constants

<a id="oelint_parser.constants.Constants.GetByPath"></a>

#### GetByPath

```python
def GetByPath(path: str) -> Union[Dict, List]
```

Get constant from path

**Arguments**:

- `path` _str_ - / joined path in the constant structure
  

**Returns**:

  Union[Dict, List]: Item in structure or empty dictionary

<a id="oelint_parser.constants.Constants.AddConstants"></a>

#### AddConstants

```python
def AddConstants(_dict: dict) -> None
```

Add constants to the existing

**Arguments**:

- `dict` _dict_ - constant dictionary to add

<a id="oelint_parser.constants.Constants.RemoveConstants"></a>

#### RemoveConstants

```python
def RemoveConstants(_dict: dict) -> None
```

Remove constants from the existing

**Arguments**:

- `dict` _dict_ - constant dictionary to remove

<a id="oelint_parser.constants.Constants.OverrideConstants"></a>

#### OverrideConstants

```python
def OverrideConstants(_dict: dict) -> None
```

Override constants in the existing db

**Arguments**:

- `dict` _dict]_ - constant dictionary with override values

<a id="oelint_parser.constants.Constants.FunctionsKnown"></a>

#### FunctionsKnown

```python
@property
def FunctionsKnown() -> List[str]
```

Return known functions

**Returns**:

- `list` - list of known functions

<a id="oelint_parser.constants.Constants.FunctionsOrder"></a>

#### FunctionsOrder

```python
@property
def FunctionsOrder() -> List[str]
```

Return function order

**Returns**:

- `list` - List of functions to order in their designated order

<a id="oelint_parser.constants.Constants.VariablesMandatory"></a>

#### VariablesMandatory

```python
@property
def VariablesMandatory() -> List[str]
```

Return mandatory variables

**Returns**:

- `list` - List of mandatory variables

<a id="oelint_parser.constants.Constants.VariablesSuggested"></a>

#### VariablesSuggested

```python
@property
def VariablesSuggested() -> List[str]
```

Return suggested variables

**Returns**:

- `list` - List of suggested variables

<a id="oelint_parser.constants.Constants.MirrorsKnown"></a>

#### MirrorsKnown

```python
@property
def MirrorsKnown() -> Dict[str, str]
```

Return known mirrors and their replacements

**Returns**:

- `dict` - Dict of known mirrors and their replacements

<a id="oelint_parser.constants.Constants.VariablesProtected"></a>

#### VariablesProtected

```python
@property
def VariablesProtected() -> List[str]
```

Return protected variables

**Returns**:

- `list` - List of protected variables

<a id="oelint_parser.constants.Constants.VariablesProtectedAppend"></a>

#### VariablesProtectedAppend

```python
@property
def VariablesProtectedAppend() -> List[str]
```

Return protected variables in bbappend files

**Returns**:

- `list` - List of protected variables in bbappend files

<a id="oelint_parser.constants.Constants.VariablesOrder"></a>

#### VariablesOrder

```python
@property
def VariablesOrder() -> List[str]
```

Variable order

**Returns**:

- `list` - List of variables to order in their designated order

<a id="oelint_parser.constants.Constants.VariablesKnown"></a>

#### VariablesKnown

```python
@property
def VariablesKnown() -> List[str]
```

Known variables

**Returns**:

- `list` - List of known variables

<a id="oelint_parser.constants.Constants.DistrosKnown"></a>

#### DistrosKnown

```python
@property
def DistrosKnown() -> List[str]
```

Known distros

**Returns**:

- `list` - List of known distros

<a id="oelint_parser.constants.Constants.MachinesKnown"></a>

#### MachinesKnown

```python
@property
def MachinesKnown() -> List[str]
```

Known machines

**Returns**:

- `list` - List of known machines

<a id="oelint_parser.constants.Constants.ImagesClasses"></a>

#### ImagesClasses

```python
@property
def ImagesClasses() -> List[str]
```

Classes that are used in images

**Returns**:

- `list` - Classes that are used in images

<a id="oelint_parser.constants.Constants.ImagesVariables"></a>

#### ImagesVariables

```python
@property
def ImagesVariables() -> List[str]
```

Variables that are used in images

**Returns**:

- `list` - Variables that are used in images

<a id="oelint_parser.constants.Constants.SetsBase"></a>

#### SetsBase

```python
@property
def SetsBase() -> Dict[str, str]
```

Base variable set

**Returns**:

- `dict` - dictionary with base variable set

<a id="oelint_parser.cls_item"></a>

# oelint\_parser.cls\_item

<a id="oelint_parser.cls_item.__id_regex__"></a>

#### \_\_id\_regex\_\_

noqa: P103

<a id="oelint_parser.cls_item.Item"></a>

## Item Objects

```python
class Item()
```

Base class for all Stash items

<a id="oelint_parser.cls_item.Item.__init__"></a>

#### \_\_init\_\_

```python
def __init__(origin: str,
             line: int,
             infileline: int,
             rawtext: str,
             realraw: str,
             new_style_override_syntax: bool = False) -> None
```

constructor

**Arguments**:

- `origin` _str_ - Full path of origin file
- `line` _int_ - Overall line counter
- `infileline` _int_ - Line number in file
- `rawtext` _str_ - Raw input string (except inline code blocks)
- `realraw` _str_ - Unprocessed input

**Arguments**:

- `new_style_override_syntax` _bool_ - Use ':' a override delimiter (default: {False})

<a id="oelint_parser.cls_item.Item.Line"></a>

#### Line

```python
@property
def Line() -> int
```

Overall line count

**Returns**:

- `int` - overall line count of item

<a id="oelint_parser.cls_item.Item.Raw"></a>

#### Raw

```python
@property
def Raw() -> str
```

Raw string (without inline code blocks)

**Returns**:

- `str` - raw string of item

<a id="oelint_parser.cls_item.Item.Origin"></a>

#### Origin

```python
@property
def Origin() -> str
```

origin of item

**Returns**:

- `str` - full path of origin file

<a id="oelint_parser.cls_item.Item.InFileLine"></a>

#### InFileLine

```python
@property
def InFileLine() -> int
```

Line count in file

**Returns**:

- `int` - [description]

<a id="oelint_parser.cls_item.Item.RealRaw"></a>

#### RealRaw

```python
@property
def RealRaw() -> str
```

Completely unprocessed raw text

**Returns**:

- `str` - completely unprocessed raw text

<a id="oelint_parser.cls_item.Item.IsFromClass"></a>

#### IsFromClass

```python
@property
def IsFromClass() -> bool
```

Item comes from a bbclass

**Returns**:

- `bool` - if item was set in a bbclass

<a id="oelint_parser.cls_item.Item.OverrideDelimiter"></a>

#### OverrideDelimiter

```python
@property
def OverrideDelimiter() -> str
```

Override delimiter

**Returns**:

- `str` - Override delimiter

<a id="oelint_parser.cls_item.Item.IsNewStyleOverrideSyntax"></a>

#### IsNewStyleOverrideSyntax

```python
@property
def IsNewStyleOverrideSyntax() -> bool
```

New style override syntax detected

**Returns**:

- `bool` - True if new style has been detected

<a id="oelint_parser.cls_item.Item.safe_linesplit"></a>

#### safe\_linesplit

```python
@staticmethod
def safe_linesplit(string: str) -> List[str]
```

Safely split an input line to chunks

**Arguments**:

- `string` _str_ - raw input string
  

**Returns**:

- `list` - list of chunks of original string

<a id="oelint_parser.cls_item.Item.get_items"></a>

#### get\_items

```python
def get_items() -> List[str]
```

Return single items

**Returns**:

- `list` - lines of raw input

<a id="oelint_parser.cls_item.Item.extract_sub"></a>

#### extract\_sub

```python
def extract_sub(name: str) -> Tuple[List[str], List[str]]
```

Extract modifiers

**Arguments**:

- `name` _str_ - input string
  

**Returns**:

- `tuple` - clean variable name, modifiers, package specific modifiers

<a id="oelint_parser.cls_item.Item.extract_sub_func"></a>

#### extract\_sub\_func

```python
def extract_sub_func(name: str) -> Tuple[List[str], List[str]]
```

Extract modifiers for functions

**Arguments**:

- `name` _str_ - input value
  

**Returns**:

- `tuple` - clean function name, modifiers

<a id="oelint_parser.cls_item.Item.IsFromAppend"></a>

#### IsFromAppend

```python
def IsFromAppend() -> bool
```

Item originates from a bbappend

**Returns**:

- `bool` - True if coming from a bbappend

<a id="oelint_parser.cls_item.Item.GetAttributes"></a>

#### GetAttributes

```python
def GetAttributes() -> dict
```

Get all public attributes of this class

**Returns**:

- `dict` - all public attributes and their values

<a id="oelint_parser.cls_item.Variable"></a>

## Variable Objects

```python
class Variable(Item)
```

Items representing variables in bitbake.

<a id="oelint_parser.cls_item.Variable.__init__"></a>

#### \_\_init\_\_

```python
def __init__(origin: str,
             line: int,
             infileline: int,
             rawtext: str,
             name: str,
             value: str,
             operator: str,
             realraw: str,
             new_style_override_syntax: bool = False) -> None
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
  

**Arguments**:

- `new_style_override_syntax` _bool_ - Use ':' a override delimiter (default: {False})

<a id="oelint_parser.cls_item.Variable.VarName"></a>

#### VarName

```python
@property
def VarName() -> str
```

Variable name

**Returns**:

- `str` - name of variable

<a id="oelint_parser.cls_item.Variable.SubItem"></a>

#### SubItem

```python
@property
def SubItem() -> str
```

Variable modifiers

**Returns**:

- `str` - variable modifiers like packages, machines, appends, prepends

<a id="oelint_parser.cls_item.Variable.SubItems"></a>

#### SubItems

```python
@property
def SubItems() -> List[str]
```

Variable modifiers list

**Returns**:

- `list` - variable modifiers list like packages, machines, appends, prepends

<a id="oelint_parser.cls_item.Variable.VarValue"></a>

#### VarValue

```python
@property
def VarValue() -> str
```

variable value

**Returns**:

- `str` - unstripped variable value

<a id="oelint_parser.cls_item.Variable.VarOp"></a>

#### VarOp

```python
@property
def VarOp() -> str
```

Variable operation

**Returns**:

- `str` - operation did on the variable

<a id="oelint_parser.cls_item.Variable.VarNameComplete"></a>

#### VarNameComplete

```python
@property
def VarNameComplete() -> str
```

Complete variable name included overrides and flags

**Returns**:

- `str` - complete variable name

<a id="oelint_parser.cls_item.Variable.VarNameCompleteNoModifiers"></a>

#### VarNameCompleteNoModifiers

```python
@property
def VarNameCompleteNoModifiers() -> str
```

Complete variable name included overrides but without modifiers like append, prepend and remove

**Returns**:

- `str` - complete variable name

<a id="oelint_parser.cls_item.Variable.RawVarName"></a>

#### RawVarName

```python
@property
def RawVarName() -> str
```

Variable name and flags combined

**Returns**:

- `str` - raw representation of the variable name

<a id="oelint_parser.cls_item.Variable.VarValueStripped"></a>

#### VarValueStripped

```python
@property
def VarValueStripped() -> str
```

Stripped variable value

**Returns**:

- `str` - stripped version of variable value

<a id="oelint_parser.cls_item.Variable.IsAppend"></a>

#### IsAppend

```python
def IsAppend() -> bool
```

Check if operation is an append

**Returns**:

- `bool` - True is variable is appended

<a id="oelint_parser.cls_item.Variable.AppendOperation"></a>

#### AppendOperation

```python
def AppendOperation() -> List[str]
```

Get variable modifiers

**Returns**:

- `list` - list could contain any combination of 'append', ' += ', 'prepend' and 'remove'

<a id="oelint_parser.cls_item.Variable.get_items"></a>

#### get\_items

```python
def get_items(override: str = "", versioned: bool = False) -> List[str]
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
def IsMultiLine() -> bool
```

Check if variable has a multiline assignment

**Returns**:

- `bool` - True if multiline

<a id="oelint_parser.cls_item.Variable.GetDistroEntry"></a>

#### GetDistroEntry

```python
def GetDistroEntry() -> str
```

Get distro specific entries in variable

**Returns**:

- `str` - distro specific modifier of variable or ""

<a id="oelint_parser.cls_item.Variable.GetMachineEntry"></a>

#### GetMachineEntry

```python
def GetMachineEntry() -> str
```

Get machine specific entries in variable

**Returns**:

- `str` - machine specific modifier of variable or ""

<a id="oelint_parser.cls_item.Variable.GetClassOverride"></a>

#### GetClassOverride

```python
def GetClassOverride() -> str
```

Get class specific entries in variable

**Returns**:

- `str` - class specific modifier of variable or ""

<a id="oelint_parser.cls_item.Variable.IsImmediateModify"></a>

#### IsImmediateModify

```python
def IsImmediateModify() -> bool
```

Variable operation is done immediately

**Returns**:

- `bool` - true if it isn't a prepend/append or remove operation

<a id="oelint_parser.cls_item.Comment"></a>

## Comment Objects

```python
class Comment(Item)
```

Items representing comments in bitbake.

<a id="oelint_parser.cls_item.Comment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(origin: str,
             line: int,
             infileline: int,
             rawtext: str,
             realraw: str,
             new_style_override_syntax: bool = False) -> None
```

constructor

**Arguments**:

- `origin` _str_ - Full path to file of origin
- `line` _int_ - Overall line counter
- `infileline` _int_ - Line counter in the particular file
- `rawtext` _str_ - Raw input string (except inline code blocks)
- `realraw` _str_ - Unprocessed input
  

**Arguments**:

- `new_style_override_syntax` _bool_ - Use ':' a override delimiter (default: {False})

<a id="oelint_parser.cls_item.Comment.get_items"></a>

#### get\_items

```python
def get_items() -> List[str]
```

Get single lines of block

**Returns**:

- `list` - single lines of comment block

<a id="oelint_parser.cls_item.Include"></a>

## Include Objects

```python
class Include(Item)
```

Items that representing include/require statements.

<a id="oelint_parser.cls_item.Include.__init__"></a>

#### \_\_init\_\_

```python
def __init__(origin: str,
             line: int,
             infileline: int,
             rawtext: str,
             incname: str,
             fileincluded: str,
             statement: str,
             realraw: str,
             new_style_override_syntax: bool = False) -> None
```

constructor

**Arguments**:

- `origin` _str_ - Full path to file of origin
- `line` _int_ - Overall line counter
- `infileline` _int_ - Line counter in the particular file
- `rawtext` _str_ - Raw input string (except inline code blocks)
- `realraw` _str_ - Unprocessed input
- `incname` _str_ - raw name of the include file
- `fileincluded` _str_ - path of the file included
- `statement` _str_ - either include or require
  

**Arguments**:

- `new_style_override_syntax` _bool_ - Use ':' a override delimiter (default: {False})

<a id="oelint_parser.cls_item.Include.IncName"></a>

#### IncName

```python
@property
def IncName() -> str
```

Include name

**Returns**:

- `str` - name of the file to include/require

<a id="oelint_parser.cls_item.Include.Statement"></a>

#### Statement

```python
@property
def Statement() -> str
```

statement either include or require

**Returns**:

- `str` - include or require

<a id="oelint_parser.cls_item.Include.FileIncluded"></a>

#### FileIncluded

```python
@property
def FileIncluded() -> str
```

The file included

**Returns**:

- `str` - path to file

<a id="oelint_parser.cls_item.Include.get_items"></a>

#### get\_items

```python
def get_items() -> Tuple[str, str]
```

Get items

**Returns**:

- `list` - include name, include statement

<a id="oelint_parser.cls_item.Export"></a>

## Export Objects

```python
class Export(Item)
```

Items representing export statements in bitbake.

<a id="oelint_parser.cls_item.Export.__init__"></a>

#### \_\_init\_\_

```python
def __init__(origin: str,
             line: int,
             infileline: int,
             rawtext: str,
             name: str,
             value: str,
             realraw: str,
             new_style_override_syntax: bool = False) -> None
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
  

**Arguments**:

- `new_style_override_syntax` _bool_ - Use ':' a override delimiter (default: {False})

<a id="oelint_parser.cls_item.Export.Name"></a>

#### Name

```python
@property
def Name() -> str
```

Name of the exported var

**Returns**:

- `str` - name of the exported var

<a id="oelint_parser.cls_item.Export.Value"></a>

#### Value

```python
@property
def Value() -> str
```

value of the export

**Returns**:

- `str` - optional value of the export

<a id="oelint_parser.cls_item.Export.get_items"></a>

#### get\_items

```python
def get_items() -> Tuple[str, str]
```

Get items

**Returns**:

- `list` - include name, include statement

<a id="oelint_parser.cls_item.Function"></a>

## Function Objects

```python
class Function(Item)
```

Items representing task definitions in bitbake.

<a id="oelint_parser.cls_item.Function.__init__"></a>

#### \_\_init\_\_

```python
def __init__(origin: str,
             line: int,
             infileline: int,
             rawtext: str,
             name: str,
             body: str,
             realraw: str,
             python: bool = False,
             fakeroot: bool = False,
             new_style_override_syntax: bool = False) -> None
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
- `new_style_override_syntax` _bool_ - Use ':' a override delimiter (default: {False})

<a id="oelint_parser.cls_item.Function.IsPython"></a>

#### IsPython

```python
@property
def IsPython() -> bool
```

Is python function

**Returns**:

- `bool` - is a python function

<a id="oelint_parser.cls_item.Function.IsFakeroot"></a>

#### IsFakeroot

```python
@property
def IsFakeroot() -> bool
```

Is fakeroot function

**Returns**:

- `bool` - is a python function

<a id="oelint_parser.cls_item.Function.FuncName"></a>

#### FuncName

```python
@property
def FuncName() -> str
```

Function name

**Returns**:

- `str` - name of function

<a id="oelint_parser.cls_item.Function.FuncNameComplete"></a>

#### FuncNameComplete

```python
@property
def FuncNameComplete() -> str
```

Complete function name (including overrides)

**Returns**:

- `str` - complete name of function

<a id="oelint_parser.cls_item.Function.SubItem"></a>

#### SubItem

```python
@property
def SubItem() -> str
```

Function modifiers

**Returns**:

- `str` - function modifiers like packages, machines, appends, prepends

<a id="oelint_parser.cls_item.Function.SubItems"></a>

#### SubItems

```python
@property
def SubItems() -> List[str]
```

Function modifiers list

**Returns**:

- `list` - function modifiers list like packages, machines, appends, prepends

<a id="oelint_parser.cls_item.Function.FuncBody"></a>

#### FuncBody

```python
@property
def FuncBody() -> str
```

Function body

**Returns**:

- `str` - function body text

<a id="oelint_parser.cls_item.Function.FuncBodyStripped"></a>

#### FuncBodyStripped

```python
@property
def FuncBodyStripped() -> str
```

Stripped function body

**Returns**:

- `str` - stripped function body text

<a id="oelint_parser.cls_item.Function.FuncBodyRaw"></a>

#### FuncBodyRaw

```python
@property
def FuncBodyRaw() -> str
```

Raw function body (including brackets)

**Returns**:

- `str` - raw function body text

<a id="oelint_parser.cls_item.Function.GetDistroEntry"></a>

#### GetDistroEntry

```python
def GetDistroEntry() -> str
```

Get distro specific modifiers

**Returns**:

- `str` - distro specific modifier or ""

<a id="oelint_parser.cls_item.Function.GetMachineEntry"></a>

#### GetMachineEntry

```python
def GetMachineEntry() -> str
```

Get machine specific modifiers

**Returns**:

- `str` - machine specific modifier or ""

<a id="oelint_parser.cls_item.Function.IsAppend"></a>

#### IsAppend

```python
def IsAppend() -> bool
```

Return if function appends another function

**Returns**:

- `bool` - True is append or prepend operation

<a id="oelint_parser.cls_item.Function.get_items"></a>

#### get\_items

```python
def get_items() -> List[str]
```

Get items of function body

**Returns**:

- `list` - single lines of function body

<a id="oelint_parser.cls_item.PythonBlock"></a>

## PythonBlock Objects

```python
class PythonBlock(Item)
```

Items representing python functions in bitbake.

<a id="oelint_parser.cls_item.PythonBlock.__init__"></a>

#### \_\_init\_\_

```python
def __init__(origin: str,
             line: int,
             infileline: int,
             rawtext: str,
             name: str,
             realraw: str,
             new_style_override_syntax: bool = False) -> None
```

constructor

**Arguments**:

- `origin` _str_ - Full path to file of origin
- `line` _int_ - Overall line counter
- `infileline` _int_ - Line counter in the particular file
- `rawtext` _str_ - Raw input string (except inline code blocks)
- `realraw` _str_ - Unprocessed input
- `name` _str_ - Function name
  

**Arguments**:

- `new_style_override_syntax` _bool_ - Use ':' a override delimiter (default: {False})

<a id="oelint_parser.cls_item.PythonBlock.FuncName"></a>

#### FuncName

```python
@property
def FuncName() -> str
```

Function name

**Returns**:

- `str` - name of function

<a id="oelint_parser.cls_item.PythonBlock.get_items"></a>

#### get\_items

```python
def get_items() -> List[str]
```

Get lines of function body

**Returns**:

- `list` - lines of function body

<a id="oelint_parser.cls_item.FlagAssignment"></a>

## FlagAssignment Objects

```python
class FlagAssignment(Item)
```

Items representing flag assignments in bitbake.

<a id="oelint_parser.cls_item.FlagAssignment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(origin: str,
             line: int,
             infileline: int,
             rawtext: str,
             name: str,
             ident: str,
             value: str,
             varop: str,
             realraw: str,
             new_style_override_syntax: bool = False) -> None
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
- `varop` _str_ - variable operation
  

**Arguments**:

- `new_style_override_syntax` _bool_ - Use ':' a override delimiter (default: {False})

<a id="oelint_parser.cls_item.FlagAssignment.VarName"></a>

#### VarName

```python
@property
def VarName() -> str
```

Variable name

**Returns**:

- `str` - name of variable

<a id="oelint_parser.cls_item.FlagAssignment.Flag"></a>

#### Flag

```python
@property
def Flag() -> str
```

Flag name

**Returns**:

- `str` - Flag name

<a id="oelint_parser.cls_item.FlagAssignment.VarOp"></a>

#### VarOp

```python
@property
def VarOp() -> str
```

Modifier operation

**Returns**:

- `str` - used modifier in operation

<a id="oelint_parser.cls_item.FlagAssignment.Value"></a>

#### Value

```python
@property
def Value() -> str
```

Value

**Returns**:

- `str` - value set

<a id="oelint_parser.cls_item.FlagAssignment.ValueStripped"></a>

#### ValueStripped

```python
@property
def ValueStripped() -> str
```

Value stripped of the quotes

**Returns**:

- `str` - value set

<a id="oelint_parser.cls_item.FlagAssignment.get_items"></a>

#### get\_items

```python
def get_items() -> Tuple[str, str, str, str]
```

Get items

**Returns**:

- `list` - variable name, flag, variable operation, modification value

<a id="oelint_parser.cls_item.FunctionExports"></a>

## FunctionExports Objects

```python
class FunctionExports(Item)
```

Items representing EXPORT_FUNCTIONS in bitbake.

<a id="oelint_parser.cls_item.FunctionExports.__init__"></a>

#### \_\_init\_\_

```python
def __init__(origin: str,
             line: int,
             infileline: int,
             rawtext: str,
             name: str,
             realraw: str,
             new_style_override_syntax: bool = False) -> None
```

constructor

**Arguments**:

- `origin` _str_ - Full path to file of origin
- `line` _int_ - Overall line counter
- `infileline` _int_ - Line counter in the particular file
- `rawtext` _str_ - Raw input string (except inline code blocks)
- `realraw` _str_ - Unprocessed input
- `name` _str_ - name of function to be exported
  

**Arguments**:

- `new_style_override_syntax` _bool_ - Use ':' a override delimiter (default: {False})

<a id="oelint_parser.cls_item.FunctionExports.FuncNames"></a>

#### FuncNames

```python
@property
def FuncNames() -> str
```

Function name

**Returns**:

- `str` - names of exported functions

<a id="oelint_parser.cls_item.FunctionExports.get_items"></a>

#### get\_items

```python
def get_items() -> List[str]
```

Get items

**Returns**:

- `list` - function names

<a id="oelint_parser.cls_item.FunctionExports.get_items_unaliased"></a>

#### get\_items\_unaliased

```python
def get_items_unaliased() -> List[str]
```

Get items with their bbclass scope names

**Returns**:

- `list` - function names in the scope of a bbclass (foo becomes classname-foo in this case)

<a id="oelint_parser.cls_item.TaskAdd"></a>

## TaskAdd Objects

```python
class TaskAdd(Item)
```

Items representing addtask statements in bitbake.

<a id="oelint_parser.cls_item.TaskAdd.__init__"></a>

#### \_\_init\_\_

```python
def __init__(origin: str,
             line: int,
             infileline: int,
             rawtext: str,
             name: str,
             realraw: str,
             before: str = "",
             after: str = "",
             comment: str = "",
             new_style_override_syntax: bool = False) -> None
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
- `comment` _str_ - optional comment (default: {""})
- `new_style_override_syntax` _bool_ - Use ':' a override delimiter (default: {False})

<a id="oelint_parser.cls_item.TaskAdd.FuncName"></a>

#### FuncName

```python
@property
def FuncName() -> str
```

Function name

**Returns**:

- `str` - name of function

<a id="oelint_parser.cls_item.TaskAdd.Before"></a>

#### Before

```python
@property
def Before() -> List[str]
```

Tasks executed before

**Returns**:

- `list` - tasks to be executed before

<a id="oelint_parser.cls_item.TaskAdd.After"></a>

#### After

```python
@property
def After() -> List[str]
```

Tasks executed after

**Returns**:

- `list` - tasks to be executed after

<a id="oelint_parser.cls_item.TaskAdd.Comment"></a>

#### Comment

```python
@property
def Comment() -> str
```

Comment

**Returns**:

- `str` - comment if any

<a id="oelint_parser.cls_item.TaskAdd.get_items"></a>

#### get\_items

```python
def get_items() -> List[str]
```

get items

**Returns**:

- `list` - function name, all before statements, all after statements

<a id="oelint_parser.cls_item.TaskDel"></a>

## TaskDel Objects

```python
class TaskDel(Item)
```

Items representing deltask statements in bitbake.

<a id="oelint_parser.cls_item.TaskDel.__init__"></a>

#### \_\_init\_\_

```python
def __init__(origin: str,
             line: int,
             infileline: int,
             rawtext: str,
             name: str,
             comment: str,
             realraw: str,
             new_style_override_syntax: bool = False) -> None
```

constructor

**Arguments**:

- `origin` _str_ - Full path to file of origin
- `line` _int_ - Overall line counter
- `infileline` _int_ - Line counter in the particular file
- `rawtext` _str_ - Raw input string (except inline code blocks)
- `realraw` _str_ - Unprocessed input
- `name` _str_ - name of task to be executed
- `comment` _str_ - optional comment
  

**Arguments**:

- `new_style_override_syntax` _bool_ - Use ':' a override delimiter (default: {False})

<a id="oelint_parser.cls_item.TaskDel.FuncName"></a>

#### FuncName

```python
@property
def FuncName() -> str
```

Function name

**Returns**:

- `str` - name of function

<a id="oelint_parser.cls_item.TaskDel.Comment"></a>

#### Comment

```python
@property
def Comment() -> str
```

Comment

**Returns**:

- `str` - comment if any

<a id="oelint_parser.cls_item.TaskDel.get_items"></a>

#### get\_items

```python
def get_items() -> List[str]
```

get items

**Returns**:

- `list` - function name

<a id="oelint_parser.cls_item.MissingFile"></a>

## MissingFile Objects

```python
class MissingFile(Item)
```

Items representing missing files found while parsing.

<a id="oelint_parser.cls_item.MissingFile.__init__"></a>

#### \_\_init\_\_

```python
def __init__(origin: str,
             line: int,
             infileline: int,
             filename: str,
             statement: str,
             new_style_override_syntax: bool = False) -> None
```

constructor

**Arguments**:

- `origin` _str_ - Full path to file of origin
- `line` _int_ - Overall line counter
- `infileline` _int_ - Line counter in the particular file
- `filename` _str_ - filename of the file that can't be found
- `statement` _str_ - either include or require
  

**Arguments**:

- `new_style_override_syntax` _bool_ - Use ':' a override delimiter (default: {False})

<a id="oelint_parser.cls_item.MissingFile.Filename"></a>

#### Filename

```python
@property
def Filename() -> str
```

Filename of the file missing

**Returns**:

- `str` - filename that can't be resolved

<a id="oelint_parser.cls_item.MissingFile.Statement"></a>

#### Statement

```python
@property
def Statement() -> str
```

statement either include or require

**Returns**:

- `str` - include or require

<a id="oelint_parser.cls_item.AddPylib"></a>

## AddPylib Objects

```python
class AddPylib(Item)
```

Items representing addpylib statements in bitbake.

<a id="oelint_parser.cls_item.AddPylib.__init__"></a>

#### \_\_init\_\_

```python
def __init__(origin: str,
             line: int,
             infileline: int,
             rawtext: str,
             path: str,
             namespace: str,
             realraw: str,
             new_style_override_syntax: bool = False) -> None
```

constructor

**Arguments**:

- `origin` _str_ - Full path to file of origin
- `line` _int_ - Overall line counter
- `infileline` _int_ - Line counter in the particular file
- `rawtext` _str_ - Raw input string (except inline code blocks)
- `realraw` _str_ - Unprocessed input
- `path` _str_ - path to the namespace
- `namespace` _str_ - namespace name
  

**Arguments**:

- `new_style_override_syntax` _bool_ - Use ':' a override delimiter (default: {False})

<a id="oelint_parser.cls_item.AddPylib.Path"></a>

#### Path

```python
@property
def Path() -> str
```

Path of the library addition

**Returns**:

- `str` - path of the library addition

<a id="oelint_parser.cls_item.AddPylib.Namespace"></a>

#### Namespace

```python
@property
def Namespace() -> str
```

Namespace of the addition

**Returns**:

- `str` - Namespace of the addition

<a id="oelint_parser.cls_item.AddPylib.get_items"></a>

#### get\_items

```python
def get_items() -> Tuple[str, str]
```

Get items

**Returns**:

- `list` - library path, library namespace

<a id="oelint_parser.cls_item.Inherit"></a>

## Inherit Objects

```python
class Inherit(Item)
```

Items that representing inherit(_defer) statements.

<a id="oelint_parser.cls_item.Inherit.__init__"></a>

#### \_\_init\_\_

```python
def __init__(origin: str,
             line: int,
             infileline: int,
             rawtext: str,
             statement: str,
             classes: str,
             realraw: str,
             new_style_override_syntax: bool = False,
             inherit_file_paths: Set[str] = None) -> None
```

constructor

**Arguments**:

- `origin` _str_ - Full path to file of origin
- `line` _int_ - Overall line counter
- `infileline` _int_ - Line counter in the particular file
- `rawtext` _str_ - Raw input string (except inline code blocks)
- `realraw` _str_ - Unprocessed input
- `class` _str_ - class code to inherit
- `statement` _str_ - inherit statement (INHERIT, inherit or inherit_defer)
  

**Arguments**:

- `new_style_override_syntax` _bool_ - Use ':' a override delimiter (default: {False})
- `inherit_file_paths` _Set[str]_ - Paths of the identified inherited classes

<a id="oelint_parser.cls_item.Inherit.Class"></a>

#### Class

```python
@property
def Class() -> str
```

Class(es) to inherit

**Returns**:

- `str` - class(es) to inherit

<a id="oelint_parser.cls_item.Inherit.Statement"></a>

#### Statement

```python
@property
def Statement() -> str
```

inherit statement

**Returns**:

- `str` - inherit or inherit_defer

<a id="oelint_parser.cls_item.Inherit.FilePaths"></a>

#### FilePaths

```python
@property
def FilePaths() -> Set[str]
```

File paths to identified bbclasses

As some classes might not be resolvable in the current context
the order doesn't necessarily reflect the order of the
inherit statements

**Returns**:

- `Set[str]` - File paths to identified bbclasses

<a id="oelint_parser.cls_item.Inherit.get_items"></a>

#### get\_items

```python
def get_items() -> List[str]
```

Get items

**Returns**:

- `list` - parsed Class items

<a id="oelint_parser.cls_item.Unset"></a>

## Unset Objects

```python
class Unset(Item)
```

Items representing unset statements in bitbake.

<a id="oelint_parser.cls_item.Unset.__init__"></a>

#### \_\_init\_\_

```python
def __init__(origin: str,
             line: int,
             infileline: int,
             rawtext: str,
             name: str,
             realraw: str,
             flag: str = "",
             new_style_override_syntax: bool = False) -> None
```

constructor

**Arguments**:

- `origin` _str_ - Full path to file of origin
- `line` _int_ - Overall line counter
- `infileline` _int_ - Line counter in the particular file
- `rawtext` _str_ - Raw input string (except inline code blocks)
- `realraw` _str_ - Unprocessed input
- `name` _str_ - name of variable to be unset
  

**Arguments**:

- `flag` _str_ - Flag to unset
- `new_style_override_syntax` _bool_ - Use ':' a override delimiter (default: {False})

<a id="oelint_parser.cls_item.Unset.VarName"></a>

#### VarName

```python
@property
def VarName() -> str
```

Variable name

**Returns**:

- `str` - name of the variable

<a id="oelint_parser.cls_item.Unset.Flag"></a>

#### Flag

```python
@property
def Flag() -> str
```

Variable flag

**Returns**:

- `str` - name of the variable flag

<a id="oelint_parser.cls_item.Unset.get_items"></a>

#### get\_items

```python
def get_items() -> List[str]
```

get items

**Returns**:

- `list` - variable name, variable flag

<a id="oelint_parser.parser"></a>

# oelint\_parser.parser

<a id="oelint_parser.parser.get_full_scope"></a>

#### get\_full\_scope

```python
def get_full_scope(_string: str, offset: int, _sstart: int, _send: int) -> str
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
def prepare_lines_subparser(_iter: Iterable,
                            lineOffset: int,
                            num: int,
                            line: int,
                            raw_line: str = None,
                            negative: bool = False) -> List[str]
```

preprocess raw input

**Arguments**:

- `_iter` _iterator_ - line interator object
- `lineOffset` _int_ - current line index
- `num` _int_ - internal line counter
- `line` _int_ - input string
- `raw_line` _string, optional_ - internal line representation. Defaults to None.
- `negative` _bool_ - Negative branch inline expansion. Defaults to False
  

**Returns**:

- `list` - list of preproccessed chunks

<a id="oelint_parser.parser.prepare_lines"></a>

#### prepare\_lines

```python
def prepare_lines(_file: str,
                  lineOffset: int = 0,
                  negative: bool = False) -> List[str]
```

break raw file input into preprocessed chunks

**Arguments**:

- `_file` _string_ - Full path to file
- `lineOffset` _int, optional_ - line offset counter. Defaults to 0.
- `negative` _bool_ - Negative branch inline expansion. Defaults to False
  

**Returns**:

- `list` - preprocessed list of chunks

<a id="oelint_parser.parser.get_items"></a>

#### get\_items

```python
def get_items(stash: object,
              _file: str,
              lineOffset: int = 0,
              new_style_override_syntax: bool = False,
              negative: bool = False) -> List[Item]
```

parses file

**Arguments**:

- `stash` _oelint_parser.cls_stash.Stash_ - Stash object
- `_file` _string_ - Full path to file
- `lineOffset` _int, optional_ - line offset counter. Defaults to 0.
- `new_style_override_syntax` _bool, optional_ - default to new override syntax (default: False)
- `negative` _bool, optional_ - Negative branch inline expansion (default: False)
  

**Returns**:

- `list` - List of oelint_parser.cls_item.* representations

