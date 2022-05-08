from enum import Enum, IntEnum


class Status(IntEnum):
    NOT_ACTIVE = 0
    ACTIVE = 1


class Color(str, Enum):
    BAY = "Bay"
    SORREL = "SORREL"
    PALOMINO = "Palomino"
    DAPPLE_GRAY = "Dapple Gray"
    DUN = "Dun"
    BUCKSKIN = "Buckskin"
    ROAN = "Roan"
    PAINT = "Paint"
    APPALOOSA = "Appaloosa"
    CHESTNUT = "Chestnut"
    TRUE_WHITE = "True White"
    GREY = "Grey"
    BLACK = "Black"
    CREMELLO = "Cremello"
    BRINDLE = "Brindle"
    SILVER_DAPPLE = "Silver Dapple"
    PERLINO = "Perlino"
    CHIMERA = "Chimera"
    CHAMPAGNE = "Champagne"
    CHOCOLATE_PALOMINO = "Chocolate Palomino"
    TRUE_BLACK = "True Black"
    STRIKING_BALANCE = "Striking Balance"


class Breed(str, Enum):
    CAROLINA_MARSH_TUCKY = "Carolina Marsh Tucky"
    ARABIAN = "Arabian"
    MORGAN = "Morgan"
    FRIESIAN = "Friesian"
    GYPSY = "Gypsy"
    MARWARI = "Marwari"
    ORLOV_TROTTER = "Orlov"
    HACKNEY = "Hackney"
    ANDALUSIAN = "Andalusian"
    IRISH_THOROUGHBRED = "Irish Thoroughbred"
