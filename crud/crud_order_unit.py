from sqlalchemy.orm import Session
import json
from typing import Any, Dict, Union
import geojson
from shapely.geometry import shape
from app.crud.base import CRUDBase
from app.models import OrderUnit
from app.schemas import OrderUnitCreate, OrderUnitUpdate


def convert_geom_to_wkt(geojson_obj: Dict) -> str:
    s = json.dumps(geojson_obj)
    g1 = geojson.loads(s)
    g2 = shape(g1)
    return g2.wkt


class CRUDOrderUnit(CRUDBase[OrderUnit, OrderUnitCreate, OrderUnitUpdate]):
    def create(self, db: Session, *, obj_in: OrderUnitCreate) -> OrderUnit:
        obj_in_dict = obj_in.dict(exclude_unset=True)
        if obj_in_dict['geom_raw']:
            obj_in_dict['geom'] = convert_geom_to_wkt(obj_in_dict['geom_raw'])
        if obj_in_dict['cloud_mask_raw']:
            obj_in_dict['cloud_mask'] = convert_geom_to_wkt(obj_in_dict['cloud_mask_raw'])
        db_obj = OrderUnit(**obj_in_dict)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(self, db: Session, *, db_obj: OrderUnit, obj_in: Union[OrderUnitUpdate, Dict[str, Any]]) -> OrderUnit:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        if db_obj.geom_raw != update_data["geom_raw"]:
            update_data['geom'] = convert_geom_to_wkt(update_data['geom_raw'])
        if db_obj.cloud_mask_raw != update_data["cloud_mask_raw"]:
            update_data['cloud_mask'] = convert_geom_to_wkt(update_data['cloud_mask_raw'])
        obj_data = db_obj.json()
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


orderUnit = CRUDOrderUnit(OrderUnit)
