
from com.kimyounggoncom.models.dataset import Dataset
from com.kimyounggoncom.models.police_service import PoliceService

class PoliceController:

    dataset = Dataset()
    service =   PoliceService()
    def modeling(self, *args): 
        this = self.service.preprocess(*args)
        # self.print_this(this)
        return this
        
    @staticmethod
    def print_this(this):
        print('*' * 100)
        print(f'1. Cctv 의 type \n {type(this.cctv)} ')
        print(f'2. Cctv 의 column \n {this.cctv.columns} ')
        print(f'3. Cctv 의 상위 1개 행\n {this.cctv.head()} ')
        print(f'4. Cctv 의 null 의 갯수\n {this.cctv.isnull().sum()}개')
        print(f'5. Crime 의 type \n {type(this.crime)}')
        print(f'6. Crime 의 column \n {this.crime.columns}')
        print(f'7. Crime 의 상위 1개 행\n {this.crime.head()}개')
        print(f'8. Crime 의 null 의 갯수\n {this.crime.isnull().sum()}개')
        print(f'9. Pop 의 type \n {type(this.pop)}')
        print(f'10. Pop 의 column \n {this.pop.columns}')
        print(f'11. Pop 의 상위 1개 행\n {this.pop.head()}개')
        print(f'12. Pop 의 null 의 갯수\n {this.pop.isnull().sum()}개')
        print('*' * 100)



        
        
    
    

    