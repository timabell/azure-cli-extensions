# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.util import CLIError


def managementgroups_exception_handler(ex):
    from azext_managementgroups.managementgroups.models import ErrorResponseException
    if isinstance(ex, ErrorResponseException):
        if ex.error.error:
            raise CLIError(ex.error.error)
        else:
            raise CLIError(ex.error)
    else:
        import sys
        from six import reraise
        reraise(*sys.exc_info())
