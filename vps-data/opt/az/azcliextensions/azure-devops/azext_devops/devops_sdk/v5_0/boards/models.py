# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class BoardColumnBase(Model):

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, description=None, name=None):
        super(BoardColumnBase, self).__init__()
        self.description = description
        self.name = name


class BoardColumnCollectionResponse(Model):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'board_columns': {'key': 'boardColumns', 'type': '[BoardColumn]'},
        'eTag': {'key': 'eTag', 'type': '[str]'}
    }

    def __init__(self, _links=None, board_columns=None, eTag=None):
        super(BoardColumnCollectionResponse, self).__init__()
        self._links = _links
        self.board_columns = board_columns
        self.eTag = eTag


class BoardColumnCreate(BoardColumnBase):

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'next_column_id': {'key': 'nextColumnId', 'type': 'str'}
    }

    def __init__(self, description=None, name=None, next_column_id=None):
        super(BoardColumnCreate, self).__init__(description=description, name=name)
        self.next_column_id = next_column_id


class BoardColumnResponse(Model):

    _attribute_map = {
        'board_column': {'key': 'boardColumn', 'type': 'BoardColumn'},
        'eTag': {'key': 'eTag', 'type': '[str]'}
    }

    def __init__(self, board_column=None, eTag=None):
        super(BoardColumnResponse, self).__init__()
        self.board_column = board_column
        self.eTag = eTag


class BoardColumnUpdate(BoardColumnCreate):

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'next_column_id': {'key': 'nextColumnId', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, description=None, next_column_id=None, name=None):
        super(BoardColumnUpdate, self).__init__(description=description, next_column_id=next_column_id)
        self.name = name


class BoardItemCollectionResponse(Model):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'board_items': {'key': 'boardItems', 'type': '[BoardItem]'},
        'eTag': {'key': 'eTag', 'type': '[str]'}
    }

    def __init__(self, _links=None, board_items=None, eTag=None):
        super(BoardItemCollectionResponse, self).__init__()
        self._links = _links
        self.board_items = board_items
        self.eTag = eTag


class BoardItemIdAndType(Model):

    _attribute_map = {
        'item_id': {'key': 'itemId', 'type': 'str'},
        'item_type': {'key': 'itemType', 'type': 'str'}
    }

    def __init__(self, item_id=None, item_type=None):
        super(BoardItemIdAndType, self).__init__()
        self.item_id = item_id
        self.item_type = item_type


class BoardItemReference(BoardItemIdAndType):

    _attribute_map = {
        'item_id': {'key': 'itemId', 'type': 'str'},
        'item_type': {'key': 'itemType', 'type': 'str'},
        'unique_id': {'key': 'uniqueId', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, item_id=None, item_type=None, unique_id=None, url=None):
        super(BoardItemReference, self).__init__(item_id=item_id, item_type=item_type)
        self.unique_id = unique_id
        self.url = url


class BoardItemResponse(Model):

    _attribute_map = {
        'eTag': {'key': 'eTag', 'type': '[str]'},
        'item': {'key': 'item', 'type': 'BoardItem'}
    }

    def __init__(self, eTag=None, item=None):
        super(BoardItemResponse, self).__init__()
        self.eTag = eTag
        self.item = item


class BoardResponse(Model):

    _attribute_map = {
        'board': {'key': 'board', 'type': 'Board'},
        'eTag': {'key': 'eTag', 'type': '[str]'}
    }

    def __init__(self, board=None, eTag=None):
        super(BoardResponse, self).__init__()
        self.board = board
        self.eTag = eTag


class BoardRowBase(Model):

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, name=None):
        super(BoardRowBase, self).__init__()
        self.name = name


class BoardRowCollectionResponse(Model):

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'board_rows': {'key': 'boardRows', 'type': '[BoardRow]'},
        'eTag': {'key': 'eTag', 'type': '[str]'}
    }

    def __init__(self, _links=None, board_rows=None, eTag=None):
        super(BoardRowCollectionResponse, self).__init__()
        self._links = _links
        self.board_rows = board_rows
        self.eTag = eTag


class BoardRowCreate(BoardRowBase):

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'next_row_id': {'key': 'nextRowId', 'type': 'str'}
    }

    def __init__(self, name=None, next_row_id=None):
        super(BoardRowCreate, self).__init__(name=name)
        self.next_row_id = next_row_id


class BoardRowResponse(Model):

    _attribute_map = {
        'board_row': {'key': 'boardRow', 'type': 'BoardRow'},
        'eTag': {'key': 'eTag', 'type': '[str]'}
    }

    def __init__(self, board_row=None, eTag=None):
        super(BoardRowResponse, self).__init__()
        self.board_row = board_row
        self.eTag = eTag


class BoardRowUpdate(BoardRowCreate):

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'next_row_id': {'key': 'nextRowId', 'type': 'str'},
    }

    def __init__(self, name=None, next_row_id=None):
        super(BoardRowUpdate, self).__init__(name=name, next_row_id=next_row_id)


class CreateBoard(Model):

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, description=None, name=None):
        super(CreateBoard, self).__init__()
        self.description = description
        self.name = name


class EntityReference(Model):

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, name=None, url=None):
        super(EntityReference, self).__init__()
        self.name = name
        self.url = url


class NewBoardItem(BoardItemIdAndType):

    _attribute_map = {
        'item_id': {'key': 'itemId', 'type': 'str'},
        'item_type': {'key': 'itemType', 'type': 'str'},
        'column_id': {'key': 'columnId', 'type': 'str'},
        'next_item_unique_id': {'key': 'nextItemUniqueId', 'type': 'str'},
        'row_id': {'key': 'rowId', 'type': 'str'}
    }

    def __init__(self, item_id=None, item_type=None, column_id=None, next_item_unique_id=None, row_id=None):
        super(NewBoardItem, self).__init__(item_id=item_id, item_type=item_type)
        self.column_id = column_id
        self.next_item_unique_id = next_item_unique_id
        self.row_id = row_id


class ReferenceLinks(Model):

    _attribute_map = {
        'links': {'key': 'links', 'type': '{object}'}
    }

    def __init__(self, links=None):
        super(ReferenceLinks, self).__init__()
        self.links = links


class UpdateBoard(Model):

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, description=None, name=None):
        super(UpdateBoard, self).__init__()
        self.description = description
        self.name = name


class UpdateBoardItem(Model):

    _attribute_map = {
        'column_id': {'key': 'columnId', 'type': 'str'},
        'next_item_unique_id': {'key': 'nextItemUniqueId', 'type': 'str'},
        'row_id': {'key': 'rowId', 'type': 'str'}
    }

    def __init__(self, column_id=None, next_item_unique_id=None, row_id=None):
        super(UpdateBoardItem, self).__init__()
        self.column_id = column_id
        self.next_item_unique_id = next_item_unique_id
        self.row_id = row_id


class BoardColumn(BoardColumnBase):

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'id': {'key': 'id', 'type': 'str'},
        'next_column_id': {'key': 'nextColumnId', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, description=None, name=None, _links=None, id=None, next_column_id=None, url=None):
        super(BoardColumn, self).__init__(description=description, name=name)
        self._links = _links
        self.id = id
        self.next_column_id = next_column_id
        self.url = url


class BoardItem(BoardItemReference):

    _attribute_map = {
        'item_id': {'key': 'itemId', 'type': 'str'},
        'item_type': {'key': 'itemType', 'type': 'str'},
        'unique_id': {'key': 'uniqueId', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'board_id': {'key': 'boardId', 'type': 'int'},
        'column': {'key': 'column', 'type': 'str'},
        'next_item_unique_id': {'key': 'nextItemUniqueId', 'type': 'str'},
        'row': {'key': 'row', 'type': 'str'}
    }

    def __init__(self, item_id=None, item_type=None, unique_id=None, url=None, _links=None, board_id=None, column=None, next_item_unique_id=None, row=None):
        super(BoardItem, self).__init__(item_id=item_id, item_type=item_type, unique_id=unique_id, url=url)
        self._links = _links
        self.board_id = board_id
        self.column = column
        self.next_item_unique_id = next_item_unique_id
        self.row = row


class BoardReference(EntityReference):

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'}
    }

    def __init__(self, name=None, url=None, id=None):
        super(BoardReference, self).__init__(name=name, url=url)
        self.id = id


class BoardRow(BoardRowBase):

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'id': {'key': 'id', 'type': 'str'},
        'next_row_id': {'key': 'nextRowId', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, name=None, _links=None, id=None, next_row_id=None, url=None):
        super(BoardRow, self).__init__(name=name)
        self._links = _links
        self.id = id
        self.next_row_id = next_row_id
        self.url = url


class Board(BoardReference):

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'description': {'key': 'description', 'type': 'str'}
    }

    def __init__(self, name=None, url=None, id=None, _links=None, description=None):
        super(Board, self).__init__(name=name, url=url, id=id)
        self._links = _links
        self.description = description


__all__ = [
    'BoardColumnBase',
    'BoardColumnCollectionResponse',
    'BoardColumnCreate',
    'BoardColumnResponse',
    'BoardColumnUpdate',
    'BoardItemCollectionResponse',
    'BoardItemIdAndType',
    'BoardItemReference',
    'BoardItemResponse',
    'BoardResponse',
    'BoardRowBase',
    'BoardRowCollectionResponse',
    'BoardRowCreate',
    'BoardRowResponse',
    'BoardRowUpdate',
    'CreateBoard',
    'EntityReference',
    'NewBoardItem',
    'ReferenceLinks',
    'UpdateBoard',
    'UpdateBoardItem',
    'BoardColumn',
    'BoardItem',
    'BoardReference',
    'BoardRow',
    'Board',
]
