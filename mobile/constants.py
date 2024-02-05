from core import models

activities = {
    "sleep": {
        "icon": "babybuddy/img/crib.svg",
        "color": "purple",
        "title": "Sleep",
        "model": models.Sleep,
        "create_url": "mobile:sleep-add",
    },
    "changes": {
        "icon": "babybuddy/img/diaper.svg",
        "color": "yellow",
        "title": "Diaper",
        "model": models.DiaperChange,
        "create_url": "mobile:changes-add",
    },
    "bottle": {
        "icon": "babybuddy/img/feeding.svg",
        "color": "green",
        "title": "Bottle Feeding",
        "model": models.Feeding,
        "create_url": "mobile:bottle-feeding-add",
    },
    "nursing": {
        "icon": "babybuddy/img/nursing.svg",
        "color": "green",
        "title": "Nursing",
        "model": models.Feeding,
        "create_url": "mobile:feeding-add",
    },
    "feeding": {
        "icon": "babybuddy/img/nursing.svg",
        "color": "green",
        "title": "Feeding",
        "model": models.Feeding,
        "create_url": "mobile:feeding-add",
    },
    "tummy": {
        "icon": "babybuddy/img/tummy.svg",
        "color": "purple",
        "title": "Tummy Time",
        "model": models.TummyTime,
        "create_url": "mobile:tummy-time-add",
    },
    "pumping": {
        "icon": "babybuddy/img/feeding.svg",
        "color": "green",
        "title": "Pumping",
        "model": models.Pumping,
        "create_url": "mobile:pumping-add",
    },
}
