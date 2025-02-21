
import pandas as pd

from com.kimyounggoncom.models.data_reader import DataReader
from com.kimyounggoncom.models.dataset import Dataset



class PoliceService:
#self는 서비스 , this 는 dataset
    reader = DataReader()
    dataset = Dataset()

    def new_model(self, fname) -> object:
        reader = self.reader
        # print(f"😎🥇🐰파일명 : {fname}")
        reader.fname = fname
        if fname.endswith('csv'):
            return reader.csv_to_dframe()
        elif fname.endswith('xls'):
            return reader.xls_to_dframe(header=2, usecols= 'B,D,G,J,N') 
    
    def preprocess(self, *args) -> object:
        print("----------모델 전처리 시작---------")
        temp = []
        for i in list(args):
            # print(f"args 값 출력: {i}")
            temp.append(i)
        # print("🤗🙂😒💸",temp)

        this = self.dataset
        this.cctv = self.new_model(temp[0])
        this = self.cctv_ratio(this)
        this.crime = self.new_model(temp[1])
        this = self.crime_ratio(this)
        this.pop = self.new_model(temp[2])
        this = self.pop_ratio(this)
        return this
    
    @staticmethod
    def cctv_ratio(this) -> object:
        
        this.cctv = this.cctv.drop(["2013년도 이전", '2014년','2015년', '2016년'], axis=1)
        print(f"CCTV 데이터 헤드: {this.cctv.head()}")
        cctv = this.cctv
        
        
        return this
    
    @staticmethod
    def crime_ratio(this) -> object:
        print(f"CRIME 데이터 헤드: {this.crime.head()}")
        crime = this.crime
        station_names = [] # 경찰서 관서명 리스트
        for name in crime['관서명']:
            station_names.append('서울' + str(name[:-1]) + '경찰서' )
        print(f"🤩🤔🎒🤦‍♀️경찰서 관서명 리스트:{station_names}")
        station_addrs = []
        station_lats = []
        station_langs = []
        # gmaps = DataReader.create_gmaps()
        return this
    
    @staticmethod
    def pop_ratio(this) -> object:
        pop = this.pop
        pop.rename(columns = {
            # pop.columns[0]: '자치구', #변경하지 않음
            pop.columns[1]: '인구수',
            pop.columns[2]: '한국인',
            pop.columns[3]: '외국인',
            pop.columns[4]: '고령자',}, inplace = True)
        print(f"POP 데이터 헤드: {this.pop.head()}")
        return this
    
    @staticmethod
    def null_check(this):
        [print(i.isnull().sum()) for i in [this.cctv, this.crime, this.pop]]
        
