
import os
import pandas as pd

from com.kimyounggoncom.models.data_reader import DataReader
from com.kimyounggoncom.models.dataset import Dataset
from com.kimyounggoncom.models.gogle_singleton import KeyRetrieverSingleton




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
        station_lngs = []

        singleton1 = KeyRetrieverSingleton()
        singleton2 = KeyRetrieverSingleton()

        

        gmaps = DataReader.create_gmaps()
        for name in station_names:
            tmp = gmaps.geocode(name, language = 'ko')
            print(f"""{name}의 검색 결과: {tmp[0].get("formatted_address")}""")
            station_addrs.append(tmp[0].get("formatted_address"))
            tmp_loc = tmp[0].get("geometry")
            station_lats.append(tmp_loc['location']['lat'])
            station_lngs.append(tmp_loc['location']['lng'])
        print(f"🐻🐻🐻자치구 리스트: {station_addrs}")
        gu_names = []
        for addr in station_addrs:
            tmp = addr.split()
            tmp_gu = [gu for gu in tmp if gu[-1] == '구'][0]
            gu_names.append(tmp_gu)
        [print(f"❤️❤️자치구 리스트 2 : {gu_names}")]
        crime['자치구'] = gu_names
        
        save_dir ="C:\\Users\\bitcamp\\Documents\\yg20250220\\com\\kimyounggoncom\\saved_data"

        if not os.path.exists(save_dir):
           os.makedirs(save_dir)
        
        crime['자치구'] = gu_names
        crime.to_csv(os.path.join(save_dir, "police_position.csv"), index=False) #내가 있는 위치에서 position_police에 대한 데이터를 saved_data에 올려줘.....올릴 때는 점 두개 쓰고 /를 쓴다.
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
        
