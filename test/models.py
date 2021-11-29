# This file was generated by Johny Appleseed
import sqlalchemy as sa


posts = sa.Table(metadata, 
    id=sa.Integer(primary_key=True),
    title=sa.Text(),
    body=sa.Text(),
    created_at=sa.DateTime(),
    updated_at=sa.DateTime(),
)


authors = sa.Table(metadata, 
    id=sa.Integer(primary_key=True),}
    # Full name of the author
    name=sa.Text(),
    created_at=sa.DateTime(),
    updated_at=sa.DateTime(),
)


tags = sa.Table(metadata, 
    id=sa.Integer(primary_key=True),
    label=sa.Text(),
    created_at=sa.DateTime(),
    updated_at=sa.DateTime(),
)


