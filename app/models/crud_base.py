from sqlalchemy.orm import Session


class CrudBase:

    @classmethod
    async def get_all(cls, db: Session):
        return db.query(cls).all()

    @classmethod
    async def create(cls, db: Session, **kwargs):
        db_data = cls(**kwargs)
        db.add(db_data)
        db.commit()
        db.refresh(db_data)
        return db_data

    @classmethod
    async def get_id(cls, db: Session, id: int):
        return db.query(cls).filter(cls.id == id).first()

    @classmethod
    async def remove_id(cls, db: Session, id: int):
        db.query(cls).filter(cls.id == id).delete()
        db.commit()

    @classmethod
    async def update_id(cls, db: Session, id: int, data_change: dict):
        db.query(cls).filter(cls.id == id).update(values=data_change)
        db.commit()
