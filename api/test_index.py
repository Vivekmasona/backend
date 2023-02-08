import pytest
import dune

from index import say_hello, root


@pytest.mark.asyncio
async def test_root():
    result = await root()
    assert result == {'message': dune.main()}