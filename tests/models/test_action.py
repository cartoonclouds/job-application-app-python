from seeds.factories import factory
from app.models.Action import Action
import pytest


class TestAction():
    # Constants

    # Fixtures
    @pytest.fixture(scope="function", autouse=True)
    def setup_teardown(self):
        # Setup
        action = factory(Action).create()

        yield action

        # Teardown

    # Helpers

    # Test Cases

    def test_action_has_many_children(self, setup_teardown):
        action = setup_teardown

        action.child_actions().save_many([
            factory(Action).make(),
            factory(Action).make()
        ])

        assert action.child_actions.count() == 2

    def test_action_has_one_parent(self, setup_teardown):
        parent_action = setup_teardown

        action = factory(Action).create(
            actionable_id=parent_action.get_key(),
            actionable_type=parent_action.get_table()
        )

        assert action.parent_action is not None
        assert isinstance(action.parent_action, Action)
