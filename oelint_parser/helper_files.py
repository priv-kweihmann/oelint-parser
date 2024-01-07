from deprecated import deprecated

from oelint_parser.cls_stash import Stash


@deprecated(version='3.0.0', reason='Use Stash.GetFiles instead')
def get_files(stash: Stash, *args, **kwargs):
    """Legacy interface get_files.

    Use Stash.GetFiles instead.

    Args:
        stash (Stash): Stash object

    Returns:
        Stash.GetFiles: .
    """
    return stash.GetFiles(*args, **kwargs)


@deprecated(version='3.0.0', reason='Use Stash.GetLayerRoot instead')
def get_layer_root(*args, **kwargs):
    """Legacy interface get_layer_root

    Use Stash.GetLayerRoot instead.

    Returns:
        Stash.GetLayerRoot: .
    """
    return Stash().GetLayerRoot(*args, **kwargs)


@deprecated(version='3.0.0', reason='Use Stash.FindLocalOrLayer instead')
def find_local_or_in_layer(*args, **kwargs):
    """Legacy interface find_local_or_in_layer

    Use Stash.FindLocalOrLayer instead.

    Returns:
        Stash.FindLocalOrLayer: .
    """
    return Stash().FindLocalOrLayer(*args, **kwargs)


@deprecated(version='3.0.0', reason='Use Stash._replace_with_known_mirrors instead')
def _replace_with_known_mirrors(*args, **kwargs):
    """Legacy interface _replace_with_known_mirrors

    Use Stash._replace_with_known_mirrors instead

    Returns:
        Stash._replace_with_known_mirrors: .
    """
    return Stash()._replace_with_known_mirrors(*args, **kwargs)


@deprecated(version='3.0.0', reason='Use Stash.GetScrComponents instead')
def get_scr_components(*args, **kwargs):
    """Legacy interface get_scr_components

    Use Stash.GetScrComponents instead

    Returns:
        Stash.GetScrComponents: .
    """
    return Stash().GetScrComponents(*args, **kwargs)


@deprecated(version='3.0.0', reason='Use Stash.SafeLineSplit instead')
def safe_linesplit(*args, **kwargs):
    """Legacy interface safe_linesplit

    Use Stash.SafeLineSplit instead

    Returns:
        Stash.SafeLineSplit: .
    """
    return Stash().SafeLineSplit(*args, **kwargs)


@deprecated(version='3.0.0', reason='Use Stash.GuessRecipeName instead')
def guess_recipe_name(*args, **kwargs):
    """Legacy interface guess_recipe_name

    Use Stash.GuessRecipeName instead

    Returns:
        Stash.GuessBaseRecipeName: .
    """
    return Stash().GuessRecipeName(*args, **kwargs)


@deprecated(version='3.0.0', reason='Use Stash.GuessBaseRecipeName instead')
def guess_base_recipe_name(*args, **kwargs):
    """Legacy interface guess_base_recipe_name

    Use Stash.GuessBaseRecipeName instead

    Returns:
        Stash.GuessBaseRecipeName: .
    """
    return Stash.GuessBaseRecipeName(*args, **kwargs)


@deprecated(version='3.0.0', reason='Use Stash.GuessRecipeVersion instead')
def guess_recipe_version(*args, **kwargs):
    """Legacy interface guess_recipe_version

    Use Stash.GuessRecipeVersion instead

    Returns:
        Stash.GuessRecipeVersion: .
    """
    return Stash().GuessRecipeVersion(*args, **kwargs)


@deprecated(version='3.0.0', reason='Use Stash.ExpandTerm instead')
def expand_term(stash: Stash, *args, **kwargs):
    """Legacy interface expand_term

    Use Stash.ExpandTerm instead

    Args:
        stash (Stash): Stash object

    Returns:
        Stash.ExpandTerm: .
    """
    return stash.ExpandTerm(*args, **kwargs)


@deprecated(version='3.0.0', reason='Use Stash.GetValidPackageNames instead')
def get_valid_package_names(stash: Stash, *args, **kwargs):
    """Legacy interface get_valid_package_names

    Use Stash.GetValidPackageNames instead

    Args:
        stash (Stash): Stash object

    Returns:
        Stash.GetValidPackageNames: .
    """
    return stash.GetValidPackageNames(*args, **kwargs)


@deprecated(version='3.0.0', reason='Use Stash.GetValidNamedResources instead')
def get_valid_named_resources(stash: Stash, *args, **kwargs):
    """Legacy interface get_valid_named_resources

    Use Stash.GetValidNamedResources instead

    Args:
        stash (Stash): Stash object

    Returns:
        Stash.GetValidNamedResources: .
    """
    return stash.GetValidNamedResources(*args, **kwargs)


@deprecated(version='3.0.0', reason='Use Stash.IsImage instead')
def is_image(stash: Stash, *args, **kwargs):
    """Legacy interface is_image

    Use Stash.IsImage instead

    Args:
        stash (Stash): Stash object

    Returns:
        Stash.IsImage: .
    """
    return stash.IsImage(*args, **kwargs)


@deprecated(version='3.0.0', reason='Use Stash.IsPackageGroup instead')
def is_packagegroup(stash: Stash, *args, **kwargs):
    """Legacy interface is_packagegroup

    Use Stash.IsPackageGroup instead

    Args:
        stash (Stash): Stash object

    Returns:
        Stash.IsPackageGroup: .
    """
    return stash.IsPackageGroup(*args, **kwargs)
