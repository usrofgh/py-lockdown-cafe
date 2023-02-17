from app.cafe import Cafe

from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError
)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    not_wearing_mask_count = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except (NotVaccinatedError, OutdatedVaccineError) as ex:
            return str(ex)
        except NotWearingMaskError:
            not_wearing_mask_count += 1

    if not_wearing_mask_count:
        return (f"Friends should buy "
                f"{not_wearing_mask_count} masks")

    return f"Friends can go to {cafe.name}"
