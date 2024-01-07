from deprecated import deprecated

from oelint_parser.cls_stash import Stash


@deprecated(version='3.0.0', reason='Use Stash.GetFiles instead')
def get_files(stash: Stash, *args, **kwargs):
    return stash.GetFiles(*args, **kwargs)


@deprecated(version='3.0.0', reason='Use Stash.GetLayerRoot instead')
def get_layer_root(*args, **kwargs):
    return Stash().GetLayerRoot(*args, **kwargs)


@deprecated(version='3.0.0', reason='Use Stash.FindLocalOrLayer instead')
def find_local_or_in_layer(*args, **kwargs):
    return Stash().FindLocalOrLayer(*args, **kwargs)


@deprecated(version='3.0.0', reason='Use Stash._replace_with_known_mirrors instead')
def _replace_with_known_mirrors(*args, **kwargs):
    return Stash()._replace_with_known_mirrors(*args, **kwargs)


@deprecated(version='3.0.0', reason='Use Stash.GetScrComponents instead')
def get_scr_components(*args, **kwargs):
    return Stash().GetScrComponents(*args, **kwargs)


@deprecated(version='3.0.0', reason='Use Stash.SafeLineSplit instead')
def safe_linesplit(*args, **kwargs):
    return Stash().SafeLineSplit(*args, **kwargs)


@deprecated(version='3.0.0', reason='Use Stash.GuessRecipeName instead')
def guess_recipe_name(*args, **kwargs):
    return Stash().GuessRecipeName(*args, **kwargs)


@deprecated(version='3.0.0', reason='Use Stash.GuessBaseRecipeName instead')
def guess_base_recipe_name(*args, **kwargs):
    return Stash.GuessBaseRecipeName(*args, **kwargs)


@deprecated(version='3.0.0', reason='Use Stash.GuessRecipeVersion instead')
def guess_recipe_version(*args, **kwargs):
    return Stash().GuessRecipeVersion(*args, **kwargs)


@deprecated(version='3.0.0', reason='Use Stash.ExpandTerm instead')
def expand_term(stash: Stash, *args, **kwargs):
    return stash.ExpandTerm(*args, **kwargs)


@deprecated(version='3.0.0', reason='Use Stash.GetValidPackageNames instead')
def get_valid_package_names(stash: Stash, *args, **kwargs):
    return stash.GetValidPackageNames(*args, **kwargs)


@deprecated(version='3.0.0', reason='Use Stash.GetValidNamedResources instead')
def get_valid_named_resources(stash: Stash, *args, **kwargs):
    return stash.GetValidNamedResources(*args, **kwargs)


@deprecated(version='3.0.0', reason='Use Stash.IsImage instead')
def is_image(stash: Stash, *args, **kwargs):
    return stash.IsImage(*args, **kwargs)


@deprecated(version='3.0.0', reason='Use Stash.IsPackageGroup instead')
def is_packagegroup(stash: Stash, *args, **kwargs):
    return stash.IsPackageGroup(*args, **kwargs)
