from vietlott.model.strategy.base import PredictModel

class RandomModel(PredictModel):
    def predict(self, *args, **kwargs):
        import random

        nums = list(range(self.min_val, self.max_val))
        random.shuffle(nums)
        predict_nums = nums[: self.number_predict]
        # Generate special number
        if (self.isSpecialLot()):
            if self.max_val == 35:
                special_num = random.randint(self.min_val, PredictModel.POWER_535_MAX_SPECIAL_VAL)
                predict_nums.append(special_num)
        return predict_nums
