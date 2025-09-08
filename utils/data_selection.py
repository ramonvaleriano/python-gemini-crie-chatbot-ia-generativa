class DataSelection:
    @staticmethod
    def eliminating_first_data(number_start: int, history_dict: dict) -> dict:
        if not number_start or number_start < 0:
            return history_dict

        new_history = history_dict[number_start:]

        return new_history

    def remove_history(
        self, remove_quantity: int, minimum_quantity: int, history: dict
    ) -> dict:
        if len(history) > minimum_quantity:
            new_history = self.eliminating_first_data(
                number_start=remove_quantity, history_dict=history
            )

            return new_history

        return history
