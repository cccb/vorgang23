
"""
Test Bureau Models
"""

import pytest
from model_mommy import mommy

from vorgang.repository import models as repository_models

@pytest.mark.django_db
def test_role():
    """Test role model"""
    role = repository_models.Role(name="fooo")
    role.save()

    assert role.pk


