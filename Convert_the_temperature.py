class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        #my solution
        #at first using variable to save each kelvin and Fahrenheit but
        #it takes loger so changed to below one
        return [celsius + 273.15 , celsius * 1.80 + 32.00]
        # other solution
        return [(celsius + 273.15),(celsius * 1.80 + 32.00)]