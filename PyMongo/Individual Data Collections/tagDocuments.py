from pymongo import MongoClient
from bson.objectid import ObjectId
import datetime

# Connects to online MongoDB cluster
client = MongoClient("mongodb+srv://<user>:<password>@<cluster>.mongodb.net/?retryWrites=true&w=majority")

# Uses database TWEETER
db = client["TWEETER"]

# Uses TAG collection
collection = db["TAG"]

# Insert the documents into the TAG collection
result = collection.insert_many(
    [
        {
            "_id": ObjectId("644f9a490cdfe59153b93685"),
            "name": "Anim",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2015-05-12", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("713f6848d919390906d0dfe2"),
            "name": "Dolore",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2012-04-19", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("22e70557f6a586946585b938"),
            "name": "Aliqua",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2018-07-19", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("c27ab37d7a6076a5c390b980"),
            "name": "Pariatur",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2011-07-14", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("d447b54c74ff98d5e38c66f9"),
            "name": "Ipsum",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2012-08-07", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("448cc7d33daaf74a84ec3fe7"),
            "name": "Laborum",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2016-12-04", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("e727abf1e622ec7c426c4efe"),
            "name": "Ad",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2015-07-16", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("1cac81ed7d98137c63db66e6"),
            "name": "Sed",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2019-09-04", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("f8a2956f7b5e0f92aebb888b"),
            "name": "Eu",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2014-08-17", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("30378c285bf0cf0c7db20cc4"),
            "name": "Ut",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2008-04-23", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("a5a09f9f84a52a9c70d08398"),
            "name": "Sint",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2020-05-07", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("0205641499567fe8bad35f0b"),
            "name": "Id",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2016-12-09", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("d920f7d6cfe693f2056a08fc"),
            "name": "Eu",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2021-06-22", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("fbfd4e75b941f54a4fd6c065"),
            "name": "Minim",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2015-10-10", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("aa08db6066a0067f75ad0b5e"),
            "name": "Consectetur",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2020-02-22", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("8ffc95c4004d84b07799d67b"),
            "name": "Qui",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2019-09-23", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("09cbdd9003c814a073eff854"),
            "name": "Eu",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2012-01-02", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("bf9416e4722c5dbfbd028dee"),
            "name": "Reprehenderit",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2013-01-04", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("d6788f1ef92043c91f2ca456"),
            "name": "Cillum",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2015-05-25", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("27e4ba122a4481aeb91f2aa3"),
            "name": "Id",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2018-03-02", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("97a464cc54194246221af0f5"),
            "name": "Laborum",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2017-01-03", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("97cbd422c4a0118d6e8f63da"),
            "name": "Duis",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2018-10-30", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("2482a2034ed516e8d12eba43"),
            "name": "Esse",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2016-02-12", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("a928c17ea26dc09788cfcab9"),
            "name": "Dolor",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2009-03-24", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("6a0237ec05639fb0681f4b14"),
            "name": "Consectetur",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2021-02-12", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("715e8bbe8c2bc9694afc72a2"),
            "name": "Ullamco",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2013-06-19", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("46bdd13739e669af41436fcc"),
            "name": "Duis",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2012-08-02", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("d4f6c01cd5a33c8bdfd99004"),
            "name": "Nulla",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2019-07-02", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("e0c2022480c89d6115f0a6a4"),
            "name": "Occaecat",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2015-11-10", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("35a220d27d10579f84c23a2e"),
            "name": "Do",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2018-11-29", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("bc4e4d7061e7edf1cd8da27c"),
            "name": "Anim",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2010-08-03", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("1c64a71380596482bcefdd86"),
            "name": "Fugiat",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2018-02-20", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("6d613192a673dd9ddab49b18"),
            "name": "Sint",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2017-01-07", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("b01bd624f298debb5a28d512"),
            "name": "Nulla",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2022-09-19", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("46a1d8b915a091fdf047714e"),
            "name": "Eiusmod",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2009-10-18", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("cfcae20e4628769a75cf3520"),
            "name": "Esse",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2011-05-19", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("5ead79318f53c9239eafe0d3"),
            "name": "Amet",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2021-11-19", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("d8a095779ee0476a1ac0666e"),
            "name": "Elit",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2013-05-21", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("ed66c4e3b9e4756b93323156"),
            "name": "Ex",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2015-07-22", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("4cc5f17848b934798ee61717"),
            "name": "Adipiscing",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2019-03-19", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("301177a63a9d85e0a2432f08"),
            "name": "Eiusmod",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2011-02-06", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("144baa6e9a5ab4f58330289d"),
            "name": "Enim",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2012-10-25", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("3f1e280a055dba7b7a8c4f4e"),
            "name": "Esse",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2012-10-18", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("2a62f2c4ab68a6a4eabbe858"),
            "name": "Proident",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2013-04-07", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("db4adc4b21a6863d31c51e38"),
            "name": "Laboris",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2016-09-08", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("04f4021c5db7009ddb4f39d3"),
            "name": "Nostrud",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2010-02-06", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("03219064bf4d26abe3913a7f"),
            "name": "Cupidatat",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2021-07-23", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("386dd6fb5c050badf36ad1f7"),
            "name": "Aute",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2022-09-11", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("605dd01651ef8d7a09f92747"),
            "name": "Pariatur",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2014-01-21", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("d289c49b774f86d30e2f8170"),
            "name": "Adipiscing",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2022-09-05", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("7b6cb3054d4066e97e7b79fd"),
            "name": "Duis",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2016-08-13", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("15da1327c87e59d9f35fef29"),
            "name": "Deserunt",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2021-05-31", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("7e006f4723b5ae558ddb890a"),
            "name": "Adipiscing",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2011-10-02", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("ee3a5138241daff7bd136b7d"),
            "name": "Incididunt",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2020-12-09", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("141c83b3f7c3c499e2ce8401"),
            "name": "Voluptate",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2008-02-08", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("431922f34752095840a2363a"),
            "name": "Ea",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2020-03-25", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("cbbff03955911a0d5c8f6b77"),
            "name": "Est",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2011-10-02", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("3fc81f46da7cd2ac9c1ae7df"),
            "name": "Velit",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2010-04-03", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("63382b0f09c21b4939a62364"),
            "name": "Reprehenderit",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2022-01-24", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("13d6625cae4e2964858aa8fc"),
            "name": "Dolore",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2014-03-14", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("b4898f96d416ebab419d7397"),
            "name": "Ut",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2015-08-31", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("3eeaf0ecd1bf967af38414ea"),
            "name": "Elit",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2013-10-23", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("15451e71ad89a9ae8f2467c1"),
            "name": "Qui",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2021-12-16", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("69728deec834d920432f1426"),
            "name": "Nostrud",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2017-04-25", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("62d26a01a59a970edb86dc88"),
            "name": "Elit",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2016-07-05", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("4803bd6bb0aefba4dc99ab37"),
            "name": "Excepteur",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2013-10-16", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("5d2ae7bff7758099703e7c5e"),
            "name": "Do",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2020-05-25", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("2569ae4e15f2a08243a7262c"),
            "name": "Reprehenderit",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2011-03-09", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("2a484cdcd2eaae166e99dcff"),
            "name": "Laboris",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2012-05-09", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("df295b1f58bdb47c8de3be9b"),
            "name": "Lorem",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2015-05-01", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("3b03fc9125e476fbdde7c319"),
            "name": "Consequat",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2010-11-24", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("3f6a168f7956620f0ed3b923"),
            "name": "Amet",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2018-10-14", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("bd65459a839206bf3f030eba"),
            "name": "Ipsum",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2022-05-16", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("b58ca2979e830aaeac272949"),
            "name": "Aliqua",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2015-06-04", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("07af06d7941b8bcf4032eb2d"),
            "name": "Ea",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2012-09-17", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("a8218d6226fce7c9a65f54a7"),
            "name": "Veniam",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2018-12-07", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("af7c5f025655e88aec049567"),
            "name": "Et",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2010-01-16", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("a904204f3ce08cead18582f6"),
            "name": "Elit",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2009-04-14", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("3dbb9348e120edb6cf008019"),
            "name": "Cillum",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2015-12-06", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("00d7c3e10b97bc97ad70b11b"),
            "name": "Fugiat",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2019-04-29", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("a8b25d8dfff2c044aeefb27d"),
            "name": "Dolor",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2008-11-07", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("53d67cf253ea18c8cb5d39dc"),
            "name": "Ipsum",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2018-06-26", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("f4f13e1b038ab483099d4c3e"),
            "name": "Nulla",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2009-09-24", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("8ecb697686f53e44abf05cda"),
            "name": "Cillum",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2009-07-03", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("08e04524f5101b07475b44cd"),
            "name": "Cupidatat",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2014-03-12", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("3de052a19c13c113c402b11c"),
            "name": "Lorem",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2009-04-30", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("48fe29de462d9e9389889206"),
            "name": "Culpa",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2010-08-07", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("dec55929b91a7066c8771f78"),
            "name": "Adipiscing",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2021-05-25", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("e905e6586392f6e5f96ba808"),
            "name": "Voluptate",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2019-10-24", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("e6713c0c4b57b943fca46f42"),
            "name": "Tempor",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2014-05-15", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("15cae054b4844b6c92574148"),
            "name": "Aliquip",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2018-12-31", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("c7e52586da62ba0c28bc65fe"),
            "name": "Aliquip",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2008-12-31", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("b0b27ef4bc1a6e45df9e3e72"),
            "name": "Aute",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2017-08-30", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("f323f78304832b0615a09a76"),
            "name": "Velit",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2017-05-01", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("357fa461671da14c9e62ff6e"),
            "name": "Esse",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2019-06-07", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("0959e3cf4ec8b380eaf90e31"),
            "name": "Laboris",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2010-09-16", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("6f13fc11cf38d92ac8b5795c"),
            "name": "Sint",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2022-04-06", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("08d6cd735f8b61f28974a53c"),
            "name": "Magna",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2014-08-08", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("6aa0391e601d0f135a51887d"),
            "name": "Do",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2012-12-09", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("822b14a1f11b3963078cc286"),
            "name": "Ipsum",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2012-01-16", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("ca2316f1259fb02e2f462092"),
            "name": "In",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2015-10-28", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("5c761ce0d4b06ca817ccb0bf"),
            "name": "Consequat",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2020-06-20", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("35cc255802629239e317a2ea"),
            "name": "Tempor",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2013-05-22", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("d6d8b4221eff68545cdaca4b"),
            "name": "Occaecat",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2016-03-07", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("a50f61d92e9daa7cb63ef559"),
            "name": "Velit",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2018-12-18", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("b1a811642d934df3baeda9fc"),
            "name": "Culpa",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2014-07-08", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("4f4443c824a7f8a14ef855ea"),
            "name": "Eiusmod",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2021-10-02", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("0b0bdba931ee64a6351473f7"),
            "name": "Consequat",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2010-09-06", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("70e93a85aae61d5a38537c4f"),
            "name": "Sit",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2012-12-10", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("4624f89ed72767229e167f07"),
            "name": "Pariatur",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2011-10-02", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("2824104c69084db34e5d887e"),
            "name": "Id",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2010-08-14", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("41b6d968c4b6c00b5f44cabf"),
            "name": "Anim",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2008-03-10", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("23197f28a93ca9002a47fd43"),
            "name": "Enim",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2016-11-06", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("dc178c79524cc259ee192652"),
            "name": "Nisi",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2017-10-14", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("58298ebabef46d0ee685d6fe"),
            "name": "Enim",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2010-11-29", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("dacef8524be601812072dd55"),
            "name": "Irure",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2011-07-28", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("b2680a72d07e2068ff7612cb"),
            "name": "Irure",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2012-11-11", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("da3e16a80016fa8bcbe5abe0"),
            "name": "Labore",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2018-01-14", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("2a8c7a077e7c30f91815a0a0"),
            "name": "Est",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2010-10-19", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("3182be9072503fc225d23842"),
            "name": "Fugiat",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2019-10-27", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("afd575e5aab73bd884016aee"),
            "name": "Aute",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2010-10-20", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("b8aa92b8e73abdff66336abe"),
            "name": "Sed",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2010-03-03", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("5ba6be45663be80a0e37a7c5"),
            "name": "Aliquip",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2022-08-24", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("d1e22751aaed83f0b88c4961"),
            "name": "Ad",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2008-09-27", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("911e9f5ebd9584fee19de776"),
            "name": "Reprehenderit",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2017-01-08", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("ab5e14a680e7d72d97c087b6"),
            "name": "Amet",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2019-11-27", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("e96edff50566acc843a6ecf7"),
            "name": "Velit",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2020-01-25", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("2a2b23be0b60894982571923"),
            "name": "Adipiscing",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2009-07-28", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("cefd451db70919cc4159f939"),
            "name": "Nostrud",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2009-03-15", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("25090e79a520cdcab5e7e0b2"),
            "name": "Aute",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2011-07-01", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("b597fd77c81eb663e9a1107b"),
            "name": "Sunt",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2015-07-30", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("1074b78c6e0f0f71c3edc7aa"),
            "name": "Deserunt",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2018-08-09", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("6ca013979bb23912c0704ced"),
            "name": "Labore",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2013-06-20", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("a31ee92de3eed96bbe74baa8"),
            "name": "Elit",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2012-01-10", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("4d266b67a69a7ba131a7118f"),
            "name": "Sunt",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2014-12-07", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("aec64a5f356a2fccd9597755"),
            "name": "Do",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2012-06-10", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("a020ab3ea539385f31e48ed6"),
            "name": "Ullamco",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2014-05-17", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("652f9c59deac75e9e9ed82b7"),
            "name": "Aliqua",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2020-02-22", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("37f1aeb2ba215514c729b5ca"),
            "name": "Veniam",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2022-10-26", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("350d7c7d6d0b47d83939f152"),
            "name": "Tempor",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2015-09-05", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("479e592e2426ad35bc3e8eb7"),
            "name": "Voluptate",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2010-11-30", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("b55a2bc7b18bffbcc12e8fe2"),
            "name": "Voluptate",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2017-07-15", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("07a52e215159d77125a3d89d"),
            "name": "Sed",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2020-10-06", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("168e4ec89166cb75dd45ad10"),
            "name": "Voluptate",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2018-12-02", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("ccb7643bfd53f771189f3e59"),
            "name": "Ullamco",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2010-12-14", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("91407d877979a3199705542d"),
            "name": "Velit",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2012-07-26", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("d561a53a763f3a5c62a9af94"),
            "name": "Culpa",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2012-07-20", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("4e29adedd07dbacfe2f667f5"),
            "name": "Amet",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2015-05-03", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("995e094e0fd20a12d49ff537"),
            "name": "Sed",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2010-03-23", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("cbd0a365dfaae05cf3cb7f0c"),
            "name": "Cupidatat",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2014-09-13", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("0cb6abf8cdc5c43f7ae37a60"),
            "name": "Pariatur",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2010-07-23", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("0ded6b49f4c6271bbcd1acf2"),
            "name": "Reprehenderit",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2016-03-15", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("679f048e2039c5f5415833ea"),
            "name": "Aliqua",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2016-05-18", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("f50702917eed571c039dcf2a"),
            "name": "Fugiat",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2015-11-28", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("13c8dafae4cd5eec1386eac1"),
            "name": "Veniam",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2014-08-06", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("b38984f1ac26e2a585b4aa29"),
            "name": "Deserunt",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2018-01-16", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("6792b0cd42c347226c68bfd9"),
            "name": "Magna",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2021-03-29", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("77193e0e127198ca31a9d578"),
            "name": "Sunt",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2013-09-04", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("42757074cbf1343e82b4e2c7"),
            "name": "Qui",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2018-02-02", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("a13b63bb5a118950a5c0277f"),
            "name": "Est",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2016-02-02", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("1aa79a3eb4fbdf0c98116299"),
            "name": "Amet",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2020-02-19", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("12a5beec4f4e0f6d3d0f8ca5"),
            "name": "Nisi",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2012-02-14", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("a02c29ddcc63f3cc9eb865c1"),
            "name": "Do",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2020-10-30", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("606187b321c0283e5ea0b3ef"),
            "name": "Ut",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2016-06-21", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("e64c807015d717592db36e1e"),
            "name": "Nostrud",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2011-04-15", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("e5a1a307f570c9cbae82a1f4"),
            "name": "Velit",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2022-10-28", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("55f2a084e6af9568a4cd5687"),
            "name": "Amet",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2017-02-02", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("ce872606b495941ac53dbcb2"),
            "name": "Exercitation",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2021-02-06", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("f797eec85780827064dabca5"),
            "name": "Laborum",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2009-09-22", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("5c997adbbe3f8f6d9d4e346c"),
            "name": "Minim",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2008-01-21", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("3a6f1c3b48be348d89c81dc5"),
            "name": "Velit",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2008-04-18", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("aa781139079939f5a6a1b0e7"),
            "name": "Sit",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2011-03-24", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("3bbfb93fbc7ff8530e4b38c8"),
            "name": "Commodo",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2013-04-23", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("3a10539f5371b7ebb7d2cec5"),
            "name": "Amet",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2018-03-23", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("859c9fbae81b0fd58af6f4cf"),
            "name": "Duis",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2009-06-04", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("073db072c909a60cd50544cf"),
            "name": "Nisi",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2009-06-03", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("b9f1199a62b4d0440eef4d92"),
            "name": "Et",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2022-07-16", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("ea7d1057c2e4f71f147ac029"),
            "name": "Mollit",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2011-11-02", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("ebde7b78d8aa44ffdeecfcb5"),
            "name": "Aliqua",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2018-12-08", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("b80ee8d4f2c2eaa2c54f2c8c"),
            "name": "Consequat",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2010-12-17", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("973dd561f58113aba6d890a0"),
            "name": "Enim",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2021-04-28", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("1a49d1a6f429646747304cae"),
            "name": "Cupidatat",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2008-09-15", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("6c4ffec98ca71a5e92e0fb39"),
            "name": "Veniam",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2012-07-29", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("8bcf89ff06646a10daa21b6d"),
            "name": "Consequat",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2014-12-01", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("d3d2531dfc890bac4cf5c5a7"),
            "name": "Ullamco",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2011-11-09", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("0067ec88a803e9e4cedb34c9"),
            "name": "Do",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2022-06-16", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("3cc14641e03f5e3875350c96"),
            "name": "Ea",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2011-11-08", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("e7bbe9c47196d3ec29cbd18a"),
            "name": "Esse",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2013-09-13", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("27ae0c1dd247c9d63e9a24e3"),
            "name": "Aute",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2018-06-10", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("4a37fd9fb59e059bb1edb0d5"),
            "name": "Occaecat",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2017-01-10", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("32a0d9fff962b3446c3ce733"),
            "name": "Dolore",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2021-12-18", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("55e253aabd21f05ceb6d9ec4"),
            "name": "Veniam",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2008-03-15", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("bddf80a289431e80ebc7a8e5"),
            "name": "Excepteur",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2019-12-04", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("d313e3941dbb4f1f16232351"),
            "name": "Et",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2013-09-17", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("2add23c756134b69600e2a1e"),
            "name": "Reprehenderit",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2015-08-13", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("2fb808d50cb2badc6d077e94"),
            "name": "Incididunt",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2021-12-06", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("6294e25488d5af3b8046077b"),
            "name": "Proident",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2010-08-19", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("204e041daa3e1313f03602d3"),
            "name": "Laborum",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2021-05-31", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("cc29cd589ddae703748a4ea1"),
            "name": "Aliqua",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2017-11-14", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("f0b9f1e8ad36b0bc225718e6"),
            "name": "Anim",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2008-08-16", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("7951fffae63ed39f667c6ba8"),
            "name": "Velit",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2009-10-23", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("d3a60f7a987b0a892595a2cc"),
            "name": "Amet",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2012-02-07", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("1b4887e571206216e43dc008"),
            "name": "Minim",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2013-05-12", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("27078367c10298016fe95a1d"),
            "name": "Nisi",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2019-10-27", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("21f08b1da1eee8331380345c"),
            "name": "Quis",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2014-06-06", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("3445ee00c8c168740ed5207e"),
            "name": "Tempor",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2019-07-13", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("f5c7adc4bd8f06cfe16955bc"),
            "name": "Aute",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2013-01-28", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("a25180830ed47293a87f7154"),
            "name": "In",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2011-04-27", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("350864d3d719f5c80dd83b82"),
            "name": "Cillum",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2020-12-22", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("4f0fd7388aa3ce068ddd2965"),
            "name": "Elit",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2019-03-07", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("7a0ae1851b814e55058d7d27"),
            "name": "Nostrud",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2018-02-13", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("a5145cdb43dc4533ff2a4627"),
            "name": "Nulla",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2018-12-23", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("5d9cf8525ded7a1ad11b87cc"),
            "name": "Excepteur",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2009-05-19", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("42e0eb6600bc6f1a9b9cc1d7"),
            "name": "Incididunt",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2022-11-04", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("ca9f382250f5c48db2c4763c"),
            "name": "Sit",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2019-07-09", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("f8bdf0e9c4b0f50f6d9229f5"),
            "name": "Cupidatat",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2012-04-25", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("64baa3b0cc2436233d419540"),
            "name": "Esse",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2016-06-30", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("ee3609320b254b525b6357b3"),
            "name": "Ad",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2020-09-28", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("987e2c49f1dd2628d7aa534f"),
            "name": "Pariatur",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2008-04-29", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("59df0293d08ff01a006d5e89"),
            "name": "Officia",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2009-02-07", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("24474cbf5f7c0d2b542bf344"),
            "name": "Aute",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2015-11-18", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("c3462199d294b6398c061820"),
            "name": "Ut",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2019-11-23", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("685c8e7a4efe3d4f521762d6"),
            "name": "Consequat",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2014-07-28", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("c908944e57201cbb1991aeae"),
            "name": "Cupidatat",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2012-01-28", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("8de189307ba23c52471bffcb"),
            "name": "Sed",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2020-07-19", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("96c916c083ac1e0c5bcf893e"),
            "name": "Eu",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2012-11-06", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("96a7768ce84bb95697c49f12"),
            "name": "Eu",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2020-11-18", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("02d21c71bb981a8b8c12add5"),
            "name": "In",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2009-02-05", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("353b46bd48e69aa4df30e389"),
            "name": "Tempor",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2009-12-18", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("93320cbd28d915775f0a6ff4"),
            "name": "Non",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2018-11-18", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("da78df10ef404f5a19d4f47f"),
            "name": "Reprehenderit",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2010-06-18", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("ac8f1bb0a6541d7933ace0ca"),
            "name": "Sint",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2018-05-20", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("bc763d0255d6cea0a4721161"),
            "name": "Commodo",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2015-05-02", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("b41938db686c53b5cdfb7d27"),
            "name": "Aliquip",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2011-04-06", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("b7317e6fd0cb7a34247a35be"),
            "name": "Dolore",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2011-10-11", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("e894d26bdcfe127f25683bb5"),
            "name": "Adipiscing",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2013-06-03", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("0392ed11daa3fdfd13140642"),
            "name": "Mollit",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2016-03-26", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("fb4acd49686602e3f5c0ffd3"),
            "name": "Minim",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2016-12-07", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("667fa41aa3a170d35d4fbddb"),
            "name": "Sunt",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2020-10-16", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("9238d0acfc29f487d08a44b4"),
            "name": "Culpa",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2012-07-22", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("11944ec539f361229a725873"),
            "name": "Amet",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2008-06-02", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("709756d986fa4834f4db828d"),
            "name": "Ea",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2022-07-12", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("03ac07f67798de1719299111"),
            "name": "Mollit",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2011-01-29", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("bb4be476e52694021fd4c996"),
            "name": "Non",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2020-01-27", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("409298860867c762146ea1c1"),
            "name": "Ullamco",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2017-05-27", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("85c6fbe4c44939e4ceb0b10d"),
            "name": "Ad",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2019-07-22", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("17227e5db66352b3dc1238fd"),
            "name": "Consectetur",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2010-12-02", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("cc79bc1ebe8a21a5100fd7ac"),
            "name": "Aute",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2016-02-14", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("d6fd3f6aefae3ec2f5e9e540"),
            "name": "Proident",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2014-08-31", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("a3a635bd60756e5beb189976"),
            "name": "Laborum",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2010-02-08", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("1be1fb9cffcf8e88df97d615"),
            "name": "Deserunt",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2021-03-29", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("faba81b6185ce89a69a345ef"),
            "name": "Proident",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2014-11-28", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("a89837fde04d9fe803f70689"),
            "name": "Officia",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2010-01-03", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("c6fbf2a06f29249aef193ee3"),
            "name": "Incididunt",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2016-06-30", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("f3cdb033daf021340866b859"),
            "name": "Eiusmod",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2008-11-02", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("a9a11d542466aa8c1deddc79"),
            "name": "Anim",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2016-02-29", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("41969e6ac6ae1ad44d72553b"),
            "name": "Eiusmod",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2021-05-18", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("dfbbe7edb3456f2cddd639d0"),
            "name": "Culpa",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2016-05-27", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("5f526c4d8c684f05564340c8"),
            "name": "Minim",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2008-06-19", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("e62cc73842eed0046308f6dd"),
            "name": "Nulla",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2020-11-12", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("5ac664d638b357ccaccde0df"),
            "name": "Sint",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2018-03-28", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("2d7823478ae52ab46721ba3e"),
            "name": "Labore",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2008-12-10", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("0d429508bc6f469d5202b67d"),
            "name": "Elit",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2008-05-28", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("d752c3180a10cc41e5e58500"),
            "name": "Qui",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2020-06-12", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("37109e5ccef83ab5000f3009"),
            "name": "Anim",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2008-01-30", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("8ff7c8e10edd5410d1fc0bf5"),
            "name": "Irure",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2021-10-30", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("afbe57b0a38614d297ad2184"),
            "name": "Exercitation",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2009-09-13", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("1995d28ab012ea8d269941bc"),
            "name": "Id",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2011-03-21", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("f9e6f27bd00eee6fd12e42a1"),
            "name": "In",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2020-08-29", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("ed193b77221bea92fff944d2"),
            "name": "Labore",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2014-05-22", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("f61ce34869457ef8c8464241"),
            "name": "Dolor",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2008-08-19", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("b04d886895b2fc70e3cd9b68"),
            "name": "Dolor",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2010-05-15", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("0d7a458565decdf8f16cb461"),
            "name": "In",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2011-10-26", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("8789c51273057373f6df67ef"),
            "name": "Adipiscing",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2021-03-04", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("af95ab45daa7bb66a59db3bc"),
            "name": "Sed",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2012-05-05", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("450d478896deddb5a074a148"),
            "name": "Excepteur",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2009-02-18", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("482dfb64480bd3c0eeb91873"),
            "name": "Consectetur",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2019-11-13", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("7dea66dfd7fd4e8731ba2539"),
            "name": "Velit",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2015-07-09", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("2ed08f7023c8d91863dfb51b"),
            "name": "Nostrud",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2021-09-16", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("5ddeb7113dad7501296d039d"),
            "name": "Laboris",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2015-04-16", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("4d54b75aaf036acae28cc178"),
            "name": "Et",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2010-07-26", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("0ce66d3845467fdcb1bd104d"),
            "name": "Commodo",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2016-06-09", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("f5f445a80db85c538897abd7"),
            "name": "Ex",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2008-07-25", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("be45087a16ec548c2e153453"),
            "name": "Sed",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2013-05-21", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("582c35d2ac2ce9eac60005b5"),
            "name": "Ut",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2019-01-06", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("0ce305b98f13c4b3763c0fbe"),
            "name": "Mollit",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2012-08-08", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("43d769fa0d088b8857f859ec"),
            "name": "Aliquip",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2019-10-18", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("087265766d21ef8d5131cd8d"),
            "name": "Mollit",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2015-12-22", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("b1e333d625c3226e3f3afd22"),
            "name": "Tempor",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2017-08-11", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("22b229d901c871952d315ce1"),
            "name": "Qui",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2016-01-07", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("d7495b12e4a4a3c27d6dee61"),
            "name": "Labore",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2015-08-03", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("8eb35675b20235699a9efb46"),
            "name": "Eu",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2016-02-07", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("fd113b4f06c0392be8eb511b"),
            "name": "Deserunt",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2014-06-14", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("f3724c8d451ebeb4c10a4dfe"),
            "name": "Commodo",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2016-12-10", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("a020f60e3e57e04fd54f36fb"),
            "name": "Lorem",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2016-08-23", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("336c8091ede6fb9c025e2884"),
            "name": "Magna",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2017-12-31", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("318997b330226149a0bddea4"),
            "name": "Adipiscing",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2018-05-04", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("5adfadbe76b0de1f7368a456"),
            "name": "Aliquip",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2017-01-24", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("e3a65792c2216cae04c83e2f"),
            "name": "Elit",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2008-08-11", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("d15e038913181d2d81ae5899"),
            "name": "Tempor",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2021-12-19", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("028c69e61adb44c8f27be879"),
            "name": "Fugiat",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2017-09-15", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("c08efdf3a6cdcf162650f240"),
            "name": "In",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2008-01-17", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("5234fa34632924a407839eb2"),
            "name": "Exercitation",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2013-04-25", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("9653810a235f9671c96477a6"),
            "name": "Culpa",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2017-05-01", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("ea996300e1a0ff732f2c3834"),
            "name": "Sed",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2019-06-08", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("b6faa6622f533bad8624f755"),
            "name": "Adipiscing",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2014-03-23", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("366e38ebc386cd886d45ff68"),
            "name": "Officia",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2022-05-10", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("60bd47ff9824779cb33031a2"),
            "name": "Sunt",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2013-11-22", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("166bafcb891a58502c96e69d"),
            "name": "Sit",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2009-10-10", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("5b3f0903b39737dcc1b1f9c2"),
            "name": "Et",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2020-11-13", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("e6f7d2cbbebc7402446ec77d"),
            "name": "Eu",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2014-12-18", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("a8aa1da03af25045bbc9861f"),
            "name": "Labore",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2016-02-29", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("5b4d225dc1b039e379c83a17"),
            "name": "Deserunt",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2013-12-19", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("115cea0f6ef44effd4aa1043"),
            "name": "Deserunt",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2021-09-26", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("d1b4b2d9fd01c6e3d438edea"),
            "name": "Pariatur",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2009-10-18", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("68b179b446e45a8e252dac60"),
            "name": "Ut",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2019-11-10", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("611feb1f1d0519f9a62b4b12"),
            "name": "Ad",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2019-12-01", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("cc79f0c2f713ee8495b5cb4b"),
            "name": "Consequat",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2012-12-12", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("0088366bc46640c4db713a2c"),
            "name": "Pariatur",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2020-07-01", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("669887a13fe6aa7f0fceb4fb"),
            "name": "Aliqua",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2017-11-17", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("9ea37194aab311d5f0dcf560"),
            "name": "Occaecat",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2011-04-20", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("ff95f078fd79050cf0541620"),
            "name": "Veniam",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2010-12-26", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("d46eda7bdf761a9b8a685ca3"),
            "name": "Est",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2019-10-12", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("7cd2526b447a821e2b1e30f4"),
            "name": "Aliquip",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2015-05-16", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("c4195a9451a1a0ddda4e42d0"),
            "name": "Tempor",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2018-05-23", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("58a67f812cfa1c2a0ffde5ee"),
            "name": "Quis",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2016-12-22", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("4beb40fe0b902215e53625cf"),
            "name": "Magna",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2019-10-20", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("f258499c2fa932a323220041"),
            "name": "Veniam",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2021-02-04", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("5f33f32fdd52950d63c6b734"),
            "name": "Pariatur",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2013-11-15", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("a80c94eccee2f13a0a5f86a4"),
            "name": "Minim",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2013-07-06", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("43a527b47024247bad271479"),
            "name": "Pariatur",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2019-10-06", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("2787cd763816c09297a310e4"),
            "name": "Eiusmod",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2014-09-10", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("482cdbc3c695d423d672d6b0"),
            "name": "Ea",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2017-04-09", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("b85f187f8ef6f0759bd255d9"),
            "name": "Occaecat",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2008-12-23", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("67c1d9927f635917240f6249"),
            "name": "Aute",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2008-03-15", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("841d9d2517e9ea4a9131e4fc"),
            "name": "Esse",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2012-06-10", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("7d13a931ebe038614b212f9f"),
            "name": "Officia",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2015-11-10", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("cf3cafaac042f854aecc8316"),
            "name": "Ad",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2014-07-07", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("d9ede58f182fd974f8a08dbc"),
            "name": "Sint",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2018-02-10", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("f75167033ddbe5750c5439f0"),
            "name": "Laborum",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2013-11-29", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("b147d677d3041c84e0125c7a"),
            "name": "Consectetur",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2012-01-27", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("4c66ae2a18af384597811817"),
            "name": "Exercitation",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2021-01-22", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("454862c5eb4c71684ea9725c"),
            "name": "Sint",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2011-12-15", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("7952b07841e9043d090a48a4"),
            "name": "Consectetur",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2022-06-25", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("4423c991993d5f134ac04d61"),
            "name": "Culpa",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2016-11-05", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("c44423411c991dee5bb1fb62"),
            "name": "Occaecat",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2017-07-25", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("23318f0dbe7d5387671c10be"),
            "name": "Sit",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2017-09-14", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("1cb1326c2660d4b75155a7ea"),
            "name": "Elit",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2018-03-12", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("f30b955db06988fc79a5ca29"),
            "name": "Cillum",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2016-12-20", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("622477c7ca71371a41030f2f"),
            "name": "Reprehenderit",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2019-04-24", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("bebc62e654b5592a1feb1285"),
            "name": "Sed",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2012-01-11", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("d627e2805e9cc36ca51a19ea"),
            "name": "Occaecat",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2016-06-12", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("b7fb6f9d8c6ecc4ad9d87e22"),
            "name": "Sint",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2021-10-16", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("42d6e9bc4f37a0a8c3bf3f6f"),
            "name": "Et",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2013-07-09", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("4abfd04e32de63a88ed6f4c9"),
            "name": "Proident",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2021-05-09", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("5a218ffe53a883b20923e0c2"),
            "name": "Quis",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2017-01-27", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("3bca39c95d9a713d91b4efc6"),
            "name": "Sed",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2009-03-14", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("63ce30c34f07175f71acb4d9"),
            "name": "Aliqua",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2020-01-21", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("6f7da6f0c79c4788390eeb17"),
            "name": "Ex",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2019-03-04", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("61a6e5b78365a3353fb513df"),
            "name": "Eu",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2010-06-20", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("4a106eb9b9557140f0e9f11d"),
            "name": "Reprehenderit",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2013-02-26", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("fdf872a6d9fd08e46fc9e7b4"),
            "name": "Veniam",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2009-07-26", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("a19ac8bd0a03a166dc2fc09e"),
            "name": "Minim",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2010-04-16", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("2f0200ca9c53367f17907c2d"),
            "name": "In",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2017-04-11", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("1c14b472255b35b37108d387"),
            "name": "Aute",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2022-01-25", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("b66e245cc5986e47ccf0c4e8"),
            "name": "Ut",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2019-04-04", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("17cb135d7e35361ca6a00ef9"),
            "name": "Labore",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2014-05-26", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("4aa5d8fa1a2dc4799f926f02"),
            "name": "Minim",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2015-02-20", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("ef73b47436a0c8234058feaf"),
            "name": "In",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2010-06-09", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("dd3f697d540fdafaf450543b"),
            "name": "Ipsum",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2020-05-12", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("a3648de91befef6704e0fcd4"),
            "name": "Exercitation",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2020-09-14", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("5fc9271ecda4df5a88f6a633"),
            "name": "Labore",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2018-01-06", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("f1bfea47b7ff52712c957480"),
            "name": "Irure",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2017-01-12", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("e5567d7d9f7b0250f0a84c27"),
            "name": "Magna",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2017-05-31", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("eb68aeb9136c1d248d103f9b"),
            "name": "Nisi",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2022-04-19", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("62bd20490c4a7d14b973a7cd"),
            "name": "Ut",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2008-12-25", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("83ec0988d43dbee8fad6b34b"),
            "name": "Nulla",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2014-01-24", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("2a55db580123d120644e07df"),
            "name": "Id",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2019-05-02", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("036408ff98f8c5c10d7fda34"),
            "name": "Dolor",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2011-05-08", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("8a5620dbc324c7a52d785166"),
            "name": "Ad",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2010-10-16", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("f31bc7904ef1d30fbc0c1098"),
            "name": "Laborum",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2018-08-01", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("815f8df66c84e823f8c2684e"),
            "name": "Magna",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2013-07-23", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("232ec9bd3401587896efae04"),
            "name": "Commodo",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2018-11-09", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("cddae8830221b7a4afc3d17a"),
            "name": "Elit",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2013-12-16", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("38ed4e56df5933d287925e34"),
            "name": "Eu",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2010-03-27", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("beb162f45299921a75a85166"),
            "name": "Lorem",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2022-03-08", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("10b08d72c50e408cd338a5ac"),
            "name": "Ad",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2015-03-18", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("ddb1099e3891d988e4ce0a10"),
            "name": "Amet",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2011-02-21", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("8a637b56376383c147318b97"),
            "name": "Officia",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2018-03-19", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("6b1ad90d96dc9a664e67e1df"),
            "name": "Qui",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2016-02-03", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("f9592d5045861a6797161fd5"),
            "name": "Velit",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2010-07-28", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("067b5b42cde74dc12d233745"),
            "name": "Velit",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2020-02-13", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("c0319b57d57a9ef38bd0e65f"),
            "name": "Do",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2022-04-03", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("37da89e87267c50cf9c0e26b"),
            "name": "Eiusmod",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2011-01-08", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("b583cf85737183e4474d58ec"),
            "name": "Exercitation",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2017-06-25", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("a7293fef89c5408e0972e154"),
            "name": "Id",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2020-11-10", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("fda9e673d73ced358461ce12"),
            "name": "Esse",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2016-09-10", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("69544e7315738c9d7542231a"),
            "name": "Sit",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2010-10-17", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("e404d161024e6166f3df9b4e"),
            "name": "Est",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2020-06-10", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("19ddbc334f53c847dd60a8ee"),
            "name": "Elit",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2008-03-27", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("af99d62e43c39c17c9d786be"),
            "name": "Reprehenderit",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2015-05-28", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("ab42ce828272f0db8451ab61"),
            "name": "Dolor",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2011-11-25", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("63e9a3e822e635aa15d18a80"),
            "name": "Id",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2017-02-15", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("3c9fc7888a18e0b88ed4d785"),
            "name": "Esse",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2009-07-31", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("65ab3feab3166e15186b6350"),
            "name": "Amet",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2016-03-15", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("5e607b915c93e7abd40ee5b5"),
            "name": "Aliquip",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2022-05-14", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("aaa30afd9c58a53ed6d1d902"),
            "name": "Incididunt",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2017-01-24", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("eb065428208044b73a5bd818"),
            "name": "Voluptate",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2015-09-09", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("283b3a671ff4c8fd082f41d0"),
            "name": "Cupidatat",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2008-10-14", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("21f740fa6a105f36efa104cc"),
            "name": "Irure",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2019-06-04", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("16a6450b874cdb7e19a948fc"),
            "name": "Occaecat",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2010-12-29", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("25aa7bf55d43c1f840acf22e"),
            "name": "Laborum",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2020-01-02", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("06226b186a0dfed694805469"),
            "name": "Consectetur",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2021-10-22", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("98ab0cd1a38e948c9bf220b8"),
            "name": "Ipsum",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2013-09-09", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("a10c828157d801009ab7c988"),
            "name": "Consectetur",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2014-07-20", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("360e01b6a06aeb9e22f6bd41"),
            "name": "Velit",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2017-01-15", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("8e4edd3ebb17010c43139d9c"),
            "name": "Id",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2015-12-06", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("bf8da32b122db19632efce9a"),
            "name": "Sed",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2015-01-23", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("b82ffa0351bfe2b9eca256c4"),
            "name": "Do",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2018-07-23", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("5ea79fae7b7ea73327fd5c8b"),
            "name": "Exercitation",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2015-07-16", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("3ae2ad89c05f3ae2864720c6"),
            "name": "Voluptate",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2019-08-10", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("a5939e505a1da0c93acfebcf"),
            "name": "Deserunt",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2008-07-25", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("de451f55198136f77dbdad27"),
            "name": "Sunt",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2011-03-24", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("706adfe8a94955035035a587"),
            "name": "Sint",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2017-03-20", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("7de2d58ac8e7e1ba4c313098"),
            "name": "Nisi",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2013-02-08", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("e833b818eb700062090b8e6e"),
            "name": "Sunt",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2017-07-21", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("1aab592c45387bdfec93376e"),
            "name": "Consequat",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2012-04-23", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("6f2088178a1ae555ef2b33dc"),
            "name": "Sed",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2020-06-25", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("c1ca9576cf778321262b6bce"),
            "name": "Irure",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2015-04-24", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("7d3c3d3db5c7bf4eb52dbf1a"),
            "name": "In",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2011-02-11", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("6746d50475fadfe7cc26653c"),
            "name": "Quis",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2022-06-28", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("7e35caded1e253ae56ec1889"),
            "name": "Incididunt",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2013-05-22", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("907afcece1336ea35ae47576"),
            "name": "Pariatur",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2009-06-22", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("c74705a7800f82f710ccf256"),
            "name": "Ea",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2015-07-17", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("4193b6fa85e0c0213ad36ea9"),
            "name": "Veniam",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2022-08-05", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("bc0719ed9a9144bb77e88bbf"),
            "name": "Ut",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2013-09-09", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("17ee85358c31c423838a4d76"),
            "name": "Nulla",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2018-01-12", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("5f47be1b6be230ee97a5de60"),
            "name": "Qui",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2011-12-24", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("1e534d6e34966eb16046c12b"),
            "name": "Laborum",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2016-11-13", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("73a0bf4eb5f518ca3d864803"),
            "name": "Nostrud",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2017-05-11", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("d9a5e0030ddd27637ad9a5ae"),
            "name": "Sit",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2018-10-22", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("af0df6e0da45c464e5cd28ca"),
            "name": "In",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2012-07-21", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("9d84dc97461f7e6a45d53e3a"),
            "name": "Do",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2022-08-08", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("da126da9201a154235135fab"),
            "name": "Voluptate",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2013-03-27", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("5d515629bc16d7fcfe74f602"),
            "name": "Consequat",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2016-11-19", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("9001f7eb22771593e43fee06"),
            "name": "Proident",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2008-12-25", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("ed6f5b3a089ef217f3b84cbf"),
            "name": "Minim",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2016-03-09", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("4735ebbb854d02088f189948"),
            "name": "Anim",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2018-10-23", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("b937d41ebacd3252b8ca6b9b"),
            "name": "Occaecat",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2016-08-24", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("4f26be824ef9dc838e725b24"),
            "name": "Sunt",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2016-10-17", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("f20e8cbfeebfd6cfddbd7bfe"),
            "name": "Veniam",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2009-09-26", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("1eced1d038b90f7c3d35467b"),
            "name": "Consectetur",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2012-12-21", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("ff5508c0ed815ac25ef92cf7"),
            "name": "Reprehenderit",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2017-10-20", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("9845c63883256a9cde82924e"),
            "name": "Ipsum",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2015-12-27", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("295e536e00a1b1c12a353304"),
            "name": "Nulla",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2011-05-06", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("b2a5d675b9f5ef23d47b4e6a"),
            "name": "Fugiat",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2022-08-20", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("76348e96d6a8612a4af2b109"),
            "name": "Tempor",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2022-03-27", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("e1fb1fbc666f8c9d4e11ff6e"),
            "name": "Reprehenderit",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2011-07-05", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("b526f3fcb7d4c61f319bfb58"),
            "name": "Esse",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2013-09-15", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("be7548b95c6b98c979b7636e"),
            "name": "Qui",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2010-02-18", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("6c036532c49dac1fc900a699"),
            "name": "Occaecat",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2020-09-07", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("52ce2cac1467f3fe7d171ff7"),
            "name": "Reprehenderit",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2011-03-24", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("1020ffce7e7e00a2760f803c"),
            "name": "In",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2014-06-30", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("5af196afe180ba5daf73dbfc"),
            "name": "In",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2021-06-09", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("9fe8dd72b9094bd0802a6d94"),
            "name": "Amet",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2021-06-19", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("8f7f3ea6b61201bca7220336"),
            "name": "Voluptate",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2022-10-30", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("89052805b9102f8b57c7b612"),
            "name": "Dolor",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2012-02-19", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("eb7fa955dbe682871555e0d0"),
            "name": "Nulla",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2021-12-14", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("d2a5a5c0cc88df0663d3e238"),
            "name": "Esse",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2013-11-01", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("49b1d37935ab0b757619c367"),
            "name": "In",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2012-06-22", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("fb1d2e1fb8e61281602f2dd3"),
            "name": "Adipiscing",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2016-10-07", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("1c9aec904f340c9aa10d4152"),
            "name": "Ex",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2009-01-27", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("d725ff2b95f13bfb0c3f1761"),
            "name": "Cupidatat",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2015-09-09", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("21958ef8a4e2485b45f5dd47"),
            "name": "Aliquip",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2021-10-21", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("8f3a7e2ecdf08f9d0a3d8e22"),
            "name": "Sit",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2020-04-29", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("203ff09e581e798e02eee45f"),
            "name": "Culpa",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2013-10-30", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("116e0ba6717f6f005e962d39"),
            "name": "Culpa",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2014-08-24", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("922460da2d6cba4f0cb8c5c5"),
            "name": "Lorem",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2016-01-24", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("9e956379b47dd7f80cebffdf"),
            "name": "Deserunt",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2014-05-10", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("288dc0e553b2b3b4b2451395"),
            "name": "Eu",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2020-09-20", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("b28c6f83433868321f3c0a40"),
            "name": "Est",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2015-07-17", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("9a0e3954de286c959c2616b8"),
            "name": "Laborum",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2017-01-26", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("8dd7a96aac016067fceba5fd"),
            "name": "Commodo",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2015-09-25", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("b5b9df6a880ae8b057399455"),
            "name": "Culpa",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2014-12-18", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("52ef9f9bc3275d4190bac428"),
            "name": "Incididunt",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2021-12-06", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("79d215fc8c31631c980bf8f5"),
            "name": "Laboris",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2020-09-27", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("fa0cc4606700c54b7a272d36"),
            "name": "Labore",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2010-02-09", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("d4e9e49eeab5d2a7507422fd"),
            "name": "Laboris",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2015-12-31", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("c77a0f568233703e75b57042"),
            "name": "Excepteur",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2020-01-18", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("d8ef39d4acdd960a9f72a7f8"),
            "name": "Occaecat",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2016-08-15", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("1ce3fa84ce51a424b263aa1a"),
            "name": "Ad",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2016-07-15", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("4238cd97f5e4061deb021a28"),
            "name": "Ex",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2020-06-15", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("dfcff7ad75bcfc04d98ad1fe"),
            "name": "Cillum",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2022-06-12", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("ca096d2538af110fef8e994c"),
            "name": "Magna",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2022-07-10", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("60fcb31280cebdce7d87007e"),
            "name": "Pariatur",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2014-07-29", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("1f262e30a58ff7ec432cd43e"),
            "name": "Lorem",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2017-05-10", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("8d30f0865933b6eb0982fa06"),
            "name": "Ullamco",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2015-06-15", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("1aea4fddc53eb0d8e4619b45"),
            "name": "Enim",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2019-11-18", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("ec5eabcefeb3b262d513bad0"),
            "name": "Fugiat",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2014-06-20", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("29b43e8eda4fb6597a34605b"),
            "name": "Consequat",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2016-06-25", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("a10ee4a6a0821c1c6357f23d"),
            "name": "In",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2012-03-06", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("1be2e86fb23999b784123ae9"),
            "name": "Mollit",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2018-11-13", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("82f0e722449ffcad47d0ad19"),
            "name": "Id",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2013-04-30", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("fffe1a96469d33f8643bb3d5"),
            "name": "Est",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2011-07-04", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("ab0eef259b12848b1c6bb44f"),
            "name": "Excepteur",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2018-04-20", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("987af9b1135f7e543729e1b4"),
            "name": "Nulla",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2022-10-15", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("e2e4c5a260433fefd2aed4c9"),
            "name": "Exercitation",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2016-11-11", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("f5d32648bbc94cb72faff1af"),
            "name": "Nulla",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2018-08-25", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("8dbb44bc49250dee9299a51c"),
            "name": "Non",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2009-11-09", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("008504b94750f9065de06c6e"),
            "name": "Eu",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2014-06-25", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("3fa040e2bfbc08a496686bee"),
            "name": "Minim",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2010-03-02", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("41cf2e529341bc4e5829175a"),
            "name": "Non",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2012-05-15", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("29449f0bac52b28293aab6ce"),
            "name": "Sunt",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2011-10-15", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("ade22660c627e14037d703a8"),
            "name": "Et",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2019-04-06", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("6b1a12b922efe4885b8cef82"),
            "name": "Aliquip",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2021-05-28", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("e6a73f939bbdfc87625b7c18"),
            "name": "Cillum",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2010-10-16", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("c1995b68cc05309b714a8899"),
            "name": "Mollit",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2019-02-17", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("1d1e133bf488a0b717433ee6"),
            "name": "Amet",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2015-11-24", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("16f58b7c3271254a89408556"),
            "name": "Ipsum",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2013-09-13", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("b04e220eeebc4c4dbeba7e59"),
            "name": "Tempor",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2008-12-26", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("54396c2209ef927c84cc797c"),
            "name": "Eu",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2010-05-12", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("c363b1891f0b99d879efba19"),
            "name": "Quis",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2019-02-12", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("fa05ddcc471321697982b66c"),
            "name": "Nisi",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2014-09-11", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("951510d5476491f06a249e2d"),
            "name": "Voluptate",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2012-12-19", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("ad0a4878c2448059feb4960b"),
            "name": "Voluptate",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2008-03-29", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("c4ee0e2692b161d17f7712d4"),
            "name": "Ullamco",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2017-01-03", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("666d2361a9d2c4b7539a32b7"),
            "name": "Cillum",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2020-04-13", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("290765583365a7c1f5ef654e"),
            "name": "Tempor",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2012-09-10", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("e6488ee202308875ef3041d0"),
            "name": "Non",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2012-02-16", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("b1bf705475f0869e89a5593e"),
            "name": "Cillum",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2014-07-01", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("432b489a76cefe5fa396500b"),
            "name": "Laborum",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2013-02-15", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("f86511b7f6424e95f3aa1afb"),
            "name": "Dolore",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2013-08-20", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("e4e097506e86d342e0e6dd9a"),
            "name": "Id",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2013-07-17", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("6f9401240ea36359c1658380"),
            "name": "Esse",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2018-05-19", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("5b1872933b6675d1197b2eae"),
            "name": "Anim",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2021-02-26", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("a71c92353e376474d16cb5e2"),
            "name": "Cupidatat",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2012-05-11", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("8df66bd2d58095ffa9ffb3cd"),
            "name": "Ad",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2013-06-18", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("270c15a0acaf5f906d931465"),
            "name": "Nostrud",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2017-04-10", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("1c68a6f10e957c81cca731b8"),
            "name": "Qui",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2015-06-17", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("70b3cfcf93ca5025bda4919d"),
            "name": "Amet",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2010-10-17", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("42784ec6f30935ce93842cd8"),
            "name": "Mollit",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2019-03-02", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("021f493a163dc8cec7ab891c"),
            "name": "Incididunt",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2011-07-20", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("92790f3bf38bc13e689dd0e4"),
            "name": "Tempor",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2021-04-09", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("096c5da9d7d09b561cabced1"),
            "name": "Non",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2015-09-05", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("9351a454cf6b5bd8bb38f853"),
            "name": "Eu",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2013-04-09", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("06fd80f1ca0c413597cdd7db"),
            "name": "Velit",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2021-07-23", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("59b6b3247d52bb214a9f13eb"),
            "name": "Ea",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2018-12-23", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("d7f14337d39876e1d42c1f6a"),
            "name": "Cillum",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2017-04-01", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("3088831e078628b8edaa0665"),
            "name": "In",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2012-09-09", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("3065f4b41144a2302d535811"),
            "name": "Est",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2009-03-02", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("16071439aebd0f67499bc1b1"),
            "name": "Do",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2009-01-14", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("75f04571ce0803e4de9241c5"),
            "name": "Elit",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2022-06-17", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("60c29f6a3468edcad439acbf"),
            "name": "Non",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2009-03-04", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("abc26c35063e6bf1191f9b9b"),
            "name": "Dolor",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2020-04-21", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("fd4e3f49caf8e5ab3e4d75c9"),
            "name": "Aute",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2012-10-17", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("ae0be6cf1918d304d5e76896"),
            "name": "Tempor",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2013-10-22", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("8b12019ca99c196e38545d40"),
            "name": "Nisi",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2008-08-19", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("3875102f85e075da7c350783"),
            "name": "Minim",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2021-05-14", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("a2dd2510b3c2d4f2030a01d8"),
            "name": "Nostrud",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2020-08-11", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("82fe9dcd50e218092b60f45a"),
            "name": "Eu",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2014-06-03", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("344b4f50bd60b1f0fba52941"),
            "name": "Nostrud",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2015-03-11", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("b1556fa7187ea64bdf23e38e"),
            "name": "Culpa",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2011-04-16", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("dfa73c7b8bb2c0e80a60ceeb"),
            "name": "Magna",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2015-03-17", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("04967e3518f896320fecad11"),
            "name": "Nisi",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2016-12-30", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("7a372bc23c20714ff5f2ecb7"),
            "name": "Mollit",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2016-06-11", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("4249fc8cbb145728c255b9e5"),
            "name": "Velit",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2012-04-08", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("22530c1e27bf99279ea5197a"),
            "name": "Culpa",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2011-01-02", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("183933e0f52b42af46477172"),
            "name": "Sed",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2009-12-21", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("ef43521992605177d6236afc"),
            "name": "Non",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2008-07-01", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("bcf2f8c79e1f6de9e3613e14"),
            "name": "Dolore",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2012-04-03", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("05671718d435a950d4b7d80b"),
            "name": "Adipiscing",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2015-07-07", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("eea518a343cb4b457afac022"),
            "name": "Dolor",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2012-06-20", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("3b7f1dc518217fd9450b6141"),
            "name": "Non",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2012-08-13", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("f5e657595e608ec479d666e0"),
            "name": "Excepteur",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2021-02-06", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("ce50633cc58af505dddbe90a"),
            "name": "Incididunt",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2022-05-29", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("e476206dc140af8621199e37"),
            "name": "Officia",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2022-03-29", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("d96ee8da07580a94774040ec"),
            "name": "Est",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2015-04-21", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("7ff09f0da87869b07b620e72"),
            "name": "Enim",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2009-06-29", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("099d3741c0bfba369afce323"),
            "name": "Sint",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2008-11-11", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("3b22245d6a75d9b0462d43d3"),
            "name": "Occaecat",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2009-04-28", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("508832acef082098c549b29a"),
            "name": "Aliqua",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2009-12-01", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("17fe140d82a0ef8ae7352aa1"),
            "name": "Aute",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2019-08-21", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("fbc98d00e04c27898c6781cd"),
            "name": "Est",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2010-05-26", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("e0fbf1e08984158f91468c03"),
            "name": "Excepteur",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2017-04-22", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("8a5b1eca0f009bdf8948b003"),
            "name": "Ipsum",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2009-04-01", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("352431b82eacbcb5e2be842a"),
            "name": "Nostrud",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2020-10-18", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("e567c14abee3d7f0efc0ae7f"),
            "name": "Anim",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2017-01-21", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("6f391f7e131313f09d135ccf"),
            "name": "Id",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2008-09-25", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("683a06be93269a19305d481b"),
            "name": "Et",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2010-03-19", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("785686a2c0b61e01f8ffd90a"),
            "name": "Cupidatat",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2016-01-02", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("5e625ea335e6d2441a9e1a6e"),
            "name": "Laboris",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2012-02-06", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("22965677e4f3dc489ae12c5c"),
            "name": "Consequat",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2012-03-23", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("7b2765aaa537e2a078bb9159"),
            "name": "Sunt",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2020-07-21", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("66ab222c46f858567633b555"),
            "name": "Dolore",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2017-11-09", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("66ba95521bc7c7dec3432dff"),
            "name": "Culpa",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2014-12-12", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("fcc6284f13734f102c28303e"),
            "name": "Ea",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2016-10-12", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("b0fe7c4d0dea632f21adf2e7"),
            "name": "Magna",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2019-03-24", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("1b6fca0a0ac9e916ec8fe8c9"),
            "name": "Veniam",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2018-12-19", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("53c6edc6b6f04fa375344565"),
            "name": "Incididunt",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2011-02-07", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("b7aaeff8f69757b64f391d1e"),
            "name": "Dolore",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2022-03-21", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("d2db3b58115683fcfe49dacc"),
            "name": "Duis",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2014-03-11", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("347dfa65186e364394176475"),
            "name": "Incididunt",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2019-02-12", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("4862e0a87d16d55416885326"),
            "name": "Duis",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2009-02-27", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("33aa7b6ff923cd2e4508d7ef"),
            "name": "Quis",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2021-02-01", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("1fece1cb7a2d713bd451e52f"),
            "name": "Qui",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2022-03-13", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("030aac9f8b814b5fd38e3361"),
            "name": "Commodo",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2011-12-19", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("aa0af2bff06eb45b8b03445e"),
            "name": "Incididunt",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2022-06-08", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("aefce36d43cb19124bf39c1d"),
            "name": "Magna",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2018-07-20", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("2df95cb4309f7572297c6d19"),
            "name": "Velit",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2016-08-27", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("182e6a3453e516881fd05934"),
            "name": "In",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2010-04-04", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("0df32b07b1f098d556b3fae1"),
            "name": "Magna",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2009-10-08", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("3cd2a23661667da6bb25d805"),
            "name": "Ex",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2009-09-30", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("1de1779b437191e0749219fa"),
            "name": "Irure",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2019-08-21", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("4f1ee8d0a8b885cf7c4d9317"),
            "name": "Ipsum",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2019-05-14", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("fa96f4bc1feadd61c8f6e1fd"),
            "name": "Incididunt",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2019-09-05", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("f0f876143f09db826756a710"),
            "name": "Qui",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2015-03-03", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("5e39284b56816231d98f6fbd"),
            "name": "Exercitation",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2013-06-19", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("7ce5f5bb2e9c14b046d4ce2d"),
            "name": "Cupidatat",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2021-09-29", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("b17c3d3bc6f5f6f04bcd4586"),
            "name": "Ipsum",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2020-01-15", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("54764383e3ea5b17a3576117"),
            "name": "Minim",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2011-03-09", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("7cb21b9cbb9ba0441685cf3c"),
            "name": "Deserunt",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2017-12-12", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("aa16455b5209b313286ca147"),
            "name": "Incididunt",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2021-04-16", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("99989a48aba43fcc14ff127e"),
            "name": "Laboris",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2009-08-22", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("95d379de2f54204a97757177"),
            "name": "Consequat",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2012-08-09", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("4735d1bc49a8a769ce72e422"),
            "name": "In",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2016-01-09", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("797f10dca98e8226ad0dbf23"),
            "name": "Amet",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2019-03-19", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("6ea6431c03679ee737e81be9"),
            "name": "Commodo",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2008-07-04", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("85dec4c9f4ee73776548a8fb"),
            "name": "Fugiat",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2015-07-03", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("3eb54308e3e8a215ae98424e"),
            "name": "Sunt",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2016-05-30", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("c369bb4000e1f6ccba02a85e"),
            "name": "Proident",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2020-06-02", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("de970231f59c3bc928f8284a"),
            "name": "Occaecat",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2012-11-10", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("2d9039e841e183d72a73c517"),
            "name": "Minim",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2020-03-24", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("3cf2548002003af6b1be9513"),
            "name": "Commodo",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2019-09-18", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("ae98c43fb7c28e85d34732f4"),
            "name": "Dolor",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2010-11-04", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("fed3898beb124bfee1f8f4c2"),
            "name": "Minim",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2017-06-10", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("e8aef87f6efcd45dfcc1042c"),
            "name": "Commodo",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2010-08-05", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("4f15e61258664e10125afe2b"),
            "name": "Aute",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2020-02-08", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("643bcfe8cab69a04b0eb40fa"),
            "name": "In",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2013-09-03", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("4f3ead63c42cbbec0636b856"),
            "name": "Occaecat",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2022-09-20", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("600815e7362448be85ac7881"),
            "name": "Ad",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2017-03-28", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("16dc24dd4e7a669138e8388a"),
            "name": "Ea",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2008-02-25", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("50ec7b20f382d4a2002a4b08"),
            "name": "Enim",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2019-07-13", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("ff904b4fe08a72305d6e3b93"),
            "name": "Dolore",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2008-06-23", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("414f0038c0f211d75f0fbcc9"),
            "name": "Fugiat",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2021-03-29", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("947ec7cc33b9206d6c7ded32"),
            "name": "Lorem",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2016-10-20", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("bf8c8ea7e4595a0dcd7cbfc9"),
            "name": "Laboris",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2022-05-09", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("4718cd813bbdadb39249df88"),
            "name": "Reprehenderit",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2018-03-08", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("b72aaaa109eeb2f4236ae226"),
            "name": "Et",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2018-10-28", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("045cd6c4de96afc2515d74b1"),
            "name": "Ullamco",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2014-09-05", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("6e7be27105019eb964039814"),
            "name": "Proident",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2013-02-02", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("c09d2f94d1fdfa87ccffc727"),
            "name": "Ullamco",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2018-09-05", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("cd76294b155a445a2a5c1224"),
            "name": "In",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2018-11-24", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("187708e1e2c135a8166e45d6"),
            "name": "Amet",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2020-09-06", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("99ae2a49bf5a04094b6419a5"),
            "name": "Nulla",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2012-11-16", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("acbb00b0ae5fde3d14734aa7"),
            "name": "Tempor",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2018-10-08", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("f867fb83d0e747e98fc9a58b"),
            "name": "Nisi",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2019-12-12", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("5f54e335552de9bcf32ddf43"),
            "name": "Exercitation",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2020-01-12", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("465bd292649c44bd64f35232"),
            "name": "Sunt",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2015-06-08", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("8851364675532f2fe1359160"),
            "name": "Ad",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2013-04-14", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("cd7092da700c0c1f42029ebd"),
            "name": "Ut",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2012-05-27", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("9456696bab4427f2edd24c25"),
            "name": "Lorem",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2012-12-07", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("23cd8f31b6758a8d0a305570"),
            "name": "Ut",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2010-10-30", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("3dfbeb771d6fdde20386fdd9"),
            "name": "Excepteur",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2008-08-15", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("e5a426394cb77076cbb7e6a0"),
            "name": "Pariatur",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2017-03-04", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("948ee2f27fa1fcfda58d27dc"),
            "name": "Cupidatat",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2016-08-26", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("4bc8c7e51e71ce36d31fad5d"),
            "name": "Et",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2010-04-03", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("6d71d71a78934f4d8e599379"),
            "name": "Laboris",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2021-09-13", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("4c574b11a88e14f60e27db9e"),
            "name": "Voluptate",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2016-08-28", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("8d502877fa4aca6c6e474e37"),
            "name": "Labore",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2021-07-17", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("9d92700da530f875c459e7bd"),
            "name": "Consectetur",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2010-09-30", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("50354d478143d82e0786bd2b"),
            "name": "Et",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2008-11-07", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("d8df68a0f68ea8e96fa3d5ad"),
            "name": "Aute",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2014-09-18", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("3bd35485f7d7be563fc8938f"),
            "name": "Consectetur",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2012-06-20", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("1e08c150bd0d231f12debe95"),
            "name": "Minim",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2015-07-20", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("2c11997f53f125e79e88b15e"),
            "name": "Eiusmod",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2009-05-31", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("53103ea17934db94879ab044"),
            "name": "Et",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2010-11-25", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("e282592175cc47da58a37b66"),
            "name": "Deserunt",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2019-01-21", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("5629e8ebda84cd79df93d75f"),
            "name": "Officia",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2013-07-21", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("207bee2459d14779b2d73264"),
            "name": "Sit",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2009-09-13", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("b8555c83c30da15c2fb9d8a6"),
            "name": "Culpa",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2021-09-13", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("aee5e5ae743d5d69c9c57dab"),
            "name": "Reprehenderit",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2020-08-19", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("144e43d2bd68b1b014a11945"),
            "name": "Exercitation",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2011-12-05", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("ecf666cf4b499378743def40"),
            "name": "Non",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2009-09-17", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("b718ff74e7c4666cafdfa9f3"),
            "name": "Officia",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2012-11-01", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("0a99e5eeab7882f641426765"),
            "name": "Consectetur",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2008-11-30", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("fea1ebc911b1e0fb4205abae"),
            "name": "Laboris",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2011-06-16", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("aa213093e8d4f138812eba19"),
            "name": "Nostrud",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2011-03-15", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("ca8547fa8e9470c9d3c33a4d"),
            "name": "Elit",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2016-12-17", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("f67bb105c12aa661a04b8d1a"),
            "name": "Sint",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2010-12-04", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("b625e7b092c79524b82c3311"),
            "name": "Nostrud",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2017-12-06", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("762926dcaff3e86718fe45d6"),
            "name": "Fugiat",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2011-05-20", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("dc4bcee3307b012d699f8d78"),
            "name": "Consequat",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2019-07-15", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("4658e02fd284fe614d8ed875"),
            "name": "Sed",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2013-03-14", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("8553c5591a0f36ea393fb4ca"),
            "name": "Reprehenderit",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2021-05-06", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("ef368bab6b18fccc2d7ea773"),
            "name": "Qui",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2009-12-23", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("514f06bd418d3ab269ada2c5"),
            "name": "Reprehenderit",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2020-06-05", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("bda24bbefb7bdcae754829cd"),
            "name": "Aliqua",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2015-07-21", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("22186e3dfdc199c8cae3951e"),
            "name": "Culpa",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2013-11-23", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("fbad8beccc2cfde96d62282d"),
            "name": "Ut",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2011-10-04", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("b540215eb4e3f65ee44c0693"),
            "name": "Officia",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2015-10-12", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("04dd2d3d18e209193abe0e54"),
            "name": "Sint",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2013-10-18", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("ff7491bfdcc5eeb391295029"),
            "name": "In",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2021-10-20", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("f997eef2de248e7ecd2f0361"),
            "name": "Cupidatat",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2019-12-04", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("611adfa9376c07e8a625efe8"),
            "name": "Sunt",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2009-05-14", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("398294a0e232671a489d2e6a"),
            "name": "Mollit",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2014-04-08", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("c4fb6b11e57e8264c6ea386e"),
            "name": "Amet",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2008-02-22", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("3184876c0da6fc39bfe77103"),
            "name": "Eiusmod",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2012-11-29", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("b58b325789b1f2cfdb624f7a"),
            "name": "Ut",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2019-10-18", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("45322b78d0174b5bd140ed79"),
            "name": "Velit",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2011-06-06", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("b0489698164dd93e1b873e8c"),
            "name": "Labore",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2012-03-20", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("ac2771afe16a0bd2dc9eed97"),
            "name": "Velit",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2020-09-26", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("74abe71e6e362f334ad1d5a9"),
            "name": "Esse",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2009-09-15", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("cb76cb2ce3b5829da263eefe"),
            "name": "Veniam",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2008-06-12", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("63b367341cbe0470b234a2f0"),
            "name": "Minim",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2010-05-29", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("1b48091f7b4f27d3fbfee2fd"),
            "name": "Ad",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2012-09-13", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("bd444f6b1011f257cb7e4dd6"),
            "name": "Eiusmod",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2016-04-26", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("5f408ce48c9910d417d1b927"),
            "name": "Aute",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2016-08-02", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("bed04efe9eb70cf534d7046e"),
            "name": "Consequat",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2009-04-09", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("08d6702759ffee0f7e575651"),
            "name": "Magna",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2010-03-06", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("79b27c4882f1772b9cd77dcf"),
            "name": "Laboris",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2021-04-21", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("3afae7f57e7b2b600b154596"),
            "name": "Quis",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2015-05-12", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("806b9cd5116290d2085f75dd"),
            "name": "Id",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2009-05-08", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("66ebfc14ef96dd3ac0edbe04"),
            "name": "Dolore",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2016-12-10", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("09a4829ca36479527f7a9371"),
            "name": "Elit",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2009-03-24", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("6de2cbfc7984ea9279127680"),
            "name": "Proident",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2009-06-12", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("f0642266c7e990ad4fd9ca28"),
            "name": "Nisi",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2010-11-10", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("712db167e73959430f30e0e3"),
            "name": "Sunt",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2008-07-11", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("11aeda49f91842ade977f076"),
            "name": "Et",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2018-10-04", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("7dc12b1d50f04c4e2aba8441"),
            "name": "Ut",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2018-07-18", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("cb8fdf6308bb5b2e839b9669"),
            "name": "Nisi",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2012-11-26", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("3c04248afcb67a4fe23bd34f"),
            "name": "Ut",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2020-01-10", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("6a91edfb945ea6ac98d758b4"),
            "name": "Aliqua",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2016-10-04", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("a2c0efbd5bd72cf030f6c488"),
            "name": "Ullamco",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2010-01-12", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("ef49c25fbad38635fbcff5c7"),
            "name": "Sed",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2017-05-30", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("370159b124eaf8e0d9c2df32"),
            "name": "Ex",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2018-01-09", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("eeee1def26adc4196835d5d6"),
            "name": "Cillum",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2018-01-13", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("cb58de6822849215c56a8f12"),
            "name": "Anim",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2010-02-19", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("4ee50041732d192dc961813b"),
            "name": "Elit",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2009-12-05", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("0426b57bba6b42ac13157e87"),
            "name": "Dolor",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2022-01-08", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("1b4599c63c4c199adda83d30"),
            "name": "Dolor",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2017-10-23", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("1fba38cff0cbe1300581c824"),
            "name": "Duis",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2013-02-13", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("79bc70ebc28024c3209794a6"),
            "name": "Lorem",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2016-03-08", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("2d0e3e8e7d7450993e56addc"),
            "name": "Culpa",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2009-06-01", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("af0f72296d4a5700bab5cc36"),
            "name": "Et",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2019-08-25", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("e7e48ddaa536c7f800c6ad90"),
            "name": "Non",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2010-05-26", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("053553c9ec35c60ddb1a5bfd"),
            "name": "Laborum",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2016-08-26", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("bc905164c60ea5e7ec312f68"),
            "name": "Fugiat",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2022-10-10", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("032a7b8ef728b9d7ba17c892"),
            "name": "Culpa",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2022-09-14", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("e24c3640425e220c11eb75f5"),
            "name": "Sunt",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2018-05-24", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("af2785ebb01db8bf7ff53c91"),
            "name": "Incididunt",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2012-09-19", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("a10f6725dcd779550f661af4"),
            "name": "Consequat",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2021-02-28", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("8b29f16c8a7c92997039bee5"),
            "name": "Enim",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2012-08-01", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("a736995b76b0b426eb8b3744"),
            "name": "Voluptate",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2008-06-04", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("61ce59e631ebebf0f6a12faa"),
            "name": "Dolor",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2019-11-14", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("8f876741172876ff20031060"),
            "name": "Fugiat",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2018-01-16", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("d17b9406be99b4241d036a06"),
            "name": "Minim",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2010-11-19", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("38a5bbf0e3aa5b5ec99647c1"),
            "name": "Laborum",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2015-09-03", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("656ade76a61db6a2da9b921f"),
            "name": "Aliqua",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2010-11-14", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("bd896e171010cc016d698592"),
            "name": "Quis",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2017-05-08", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("426bfad9eef0f536581387ff"),
            "name": "Lorem",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2008-08-20", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("709154135c59135face1e8b4"),
            "name": "Commodo",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2012-11-23", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("d3c0045b771eb502a231ebb6"),
            "name": "Lorem",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2011-11-24", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("4ef93bad183e7948051e74a6"),
            "name": "Pariatur",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2018-01-23", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("f1c606755dde41aacf244188"),
            "name": "Consectetur",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2015-12-02", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("8c6960bb2bd7750b77e580bb"),
            "name": "Ea",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2021-01-26", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("c445e3bfe8cb1000976d36f1"),
            "name": "Dolore",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2016-11-16", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("f4b0f15aed02c5f50751c868"),
            "name": "Proident",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2017-06-04", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("4112aeeaab240031038ef172"),
            "name": "Ad",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2009-07-21", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("994b0a29765f9d4b06b4e2a5"),
            "name": "Laborum",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2018-01-30", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("eb041271f280ea647a20f6a9"),
            "name": "Voluptate",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2011-04-13", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("9c0514052828050fa9abe71f"),
            "name": "Pariatur",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2020-11-27", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("bb1692e53582309ce5ae920b"),
            "name": "Tempor",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2018-08-27", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("0bc03b5dcae5c484efa3ea8f"),
            "name": "Nulla",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2015-04-09", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("5e8033b7736a9d8e0f3d7b44"),
            "name": "Irure",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2018-08-09", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("094a31da3fef7e2b038086a1"),
            "name": "Deserunt",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2017-02-09", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("d495648f6914466da2e59cf2"),
            "name": "Cillum",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2008-02-27", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("d38c37a6f7acc76b594d877d"),
            "name": "Enim",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2019-02-18", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("5c7cd185123d4ef3e79fd2b2"),
            "name": "Voluptate",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2021-02-26", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("679d14fc1a311cb8d6f1c981"),
            "name": "Aliqua",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2010-02-05", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("b38e601edb3adec6ebf9c035"),
            "name": "Magna",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2011-03-14", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("e291c5a7faa2a16aa509c8c2"),
            "name": "Nisi",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2019-01-10", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("47bdecdd0d753c03951e3685"),
            "name": "Eu",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2017-11-19", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("60076b6a210aca87f1337acd"),
            "name": "Dolor",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2010-10-23", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("829a50d4ec9e57d954863b23"),
            "name": "Adipiscing",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2015-07-17", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("33c151e2467c5c8cf5fbfe72"),
            "name": "Cupidatat",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2015-09-20", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("a161c04e6a07ec836728f295"),
            "name": "Enim",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2017-10-08", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("8c1ff6373dddda8ef1ee2c7a"),
            "name": "Velit",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2009-02-24", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("e324de9ede92daf8f413466e"),
            "name": "Culpa",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2014-07-08", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("11380f20dad83c6a9b187deb"),
            "name": "Dolor",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2008-01-30", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("69c6c7745bf607bbdd3d9682"),
            "name": "Sed",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2022-05-04", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("2138dab5185a78c0e77138e7"),
            "name": "Ullamco",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2012-09-25", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("8fffce7cfe3d727f58b8f007"),
            "name": "Esse",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2015-04-03", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("c07407c3ed0dece8c2657884"),
            "name": "Anim",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2008-09-24", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("c9e55d9a6bc184b52ec809e9"),
            "name": "Reprehenderit",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2013-01-27", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("8256bb9a5ea8ad277b773a46"),
            "name": "Occaecat",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2020-12-02", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("ee1545da5bbcfe759c8b9705"),
            "name": "Ullamco",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2009-07-13", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("4d2753223665306f65a3af15"),
            "name": "Eu",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2020-07-10", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("9066f67f03b18ed9df16f317"),
            "name": "Sit",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2013-06-12", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("d1e6e4f4d648bdf4203cbc70"),
            "name": "Ad",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2008-05-11", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("27e9a5de3ad6cba9b300d90d"),
            "name": "Do",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2010-09-18", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("0f393cdb222ee30561ce0f16"),
            "name": "Esse",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2019-12-22", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("33d6390ab05d6d2420c9c1a4"),
            "name": "Labore",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2009-03-31", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("5052f071ed159e8840d27fd4"),
            "name": "Et",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2019-10-17", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("97ffb3c2df076a657afedbd9"),
            "name": "Esse",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2012-09-24", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("65784f28ecf2e6907d96a880"),
            "name": "Irure",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2021-11-06", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("f83524b64cda543688513789"),
            "name": "Pariatur",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2017-06-15", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("c1c5b9103419a3141251cded"),
            "name": "Irure",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2016-02-25", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("8ab5b8568ac53c1d84255969"),
            "name": "Occaecat",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2011-06-09", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("d7029cb6c4a19a9529f9a3a9"),
            "name": "Excepteur",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2013-06-03", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("759a4de7ed1b088354c31c60"),
            "name": "Ea",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2013-08-09", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("4b5edbc074220feee3f7e622"),
            "name": "Dolore",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2021-08-02", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("c901670809b45a8810762af2"),
            "name": "Anim",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2020-12-22", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("673239379cb1ce35d43b91e7"),
            "name": "Eiusmod",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2020-07-12", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("9b40a9df08befabc6c59b6e3"),
            "name": "Velit",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2018-09-17", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("67fecda525c4a79b739d672b"),
            "name": "Enim",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2012-06-10", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("3f9bbdda88202eff2ec1b459"),
            "name": "Sint",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2019-05-12", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("9a2c94a0fc48e2eee136f151"),
            "name": "Elit",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2022-06-10", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("1a974f94b15864b6cc75eda2"),
            "name": "Aute",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2021-04-30", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("385b2c104e40d71292293ff9"),
            "name": "Fugiat",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2013-01-14", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("f2b5f88997c8daa042d3c0e0"),
            "name": "Quis",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2013-05-07", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("02c77779a9fcaa542366fc52"),
            "name": "Elit",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2020-09-20", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("46b464ec5a6f00a571a7137f"),
            "name": "Cillum",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2021-11-04", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("3a02df91d12bdb922184aa92"),
            "name": "Duis",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2017-08-27", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("588cc28c8ae2135bf2876809"),
            "name": "Adipiscing",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2010-01-24", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("8983411d1f2874c8c788e90f"),
            "name": "Commodo",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2008-06-11", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("1b33ed211b262d4adc2fb248"),
            "name": "Cupidatat",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2011-10-21", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("33b1728b02b3e9b1da3acd33"),
            "name": "Et",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2014-12-19", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("e594c9242166ae073c8f281c"),
            "name": "Sit",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2021-09-03", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("4a14855d6e46f4a0f289814f"),
            "name": "Consectetur",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2008-11-08", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("d79839b6cd50e71af4cfc0a9"),
            "name": "Ipsum",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2019-11-14", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("1ee40b22fa8b2c19b075906b"),
            "name": "Fugiat",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2009-05-17", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("90f843d381f5ee8835e72b93"),
            "name": "Exercitation",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2018-02-14", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("01b7e44a2ac65c9156111279"),
            "name": "Cupidatat",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2011-09-14", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("9acca239b35b34f2e0bd2df8"),
            "name": "Excepteur",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2013-04-27", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("8a2fa1c5cc417edf5477446f"),
            "name": "Cillum",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2008-12-29", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("96cc6be7b5ccc924b0274fb4"),
            "name": "Proident",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2020-04-21", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("9d9ef71cbad403e50ca3033c"),
            "name": "Pariatur",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2009-04-11", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("1f88cd34d191ac3c49d60338"),
            "name": "Sed",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2021-11-30", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("df7246a8bb9809908ee5b2c5"),
            "name": "Elit",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2017-10-21", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("5bfae483ae4f5624d5e32868"),
            "name": "Magna",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2012-01-04", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("860574dce87afe3776b0db46"),
            "name": "Sunt",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2015-07-01", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("93effd817f2ef3ec21fba0a9"),
            "name": "Reprehenderit",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2021-05-27", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("18604ca0d88bb8ec5f7faf5b"),
            "name": "Culpa",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2013-02-27", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("4d20fdb8a8a19a2bd679cc26"),
            "name": "Dolore",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2013-04-01", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("94a5afc6d4ccceeb760f06f3"),
            "name": "Elit",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2013-02-07", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("4aeeebbd579f0a49e3a3305a"),
            "name": "Minim",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2012-01-27", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("dcadeae7c83dea7f8a9bb3ca"),
            "name": "Cillum",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2010-05-14", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("45f0476c322fd91f28ed11b6"),
            "name": "Adipiscing",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2010-07-24", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("64f957865c148879aff2bbba"),
            "name": "Est",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2013-12-22", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("2f7571a7e3e4227f115c4ffb"),
            "name": "Ex",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2020-01-12", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("ba09ba81e999ac8dfda1a9b3"),
            "name": "Ut",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2020-03-31", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("3539c59bc739affd4a7f257e"),
            "name": "Ex",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2020-03-04", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("9b5e069489537d848e8720a9"),
            "name": "Cupidatat",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2017-01-02", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("c180649d04293cda3e28a5cf"),
            "name": "Sint",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2010-08-14", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("e3acf91349b0e42347646886"),
            "name": "Minim",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2009-04-16", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("503f242fbc6cbb2f4112bf72"),
            "name": "Sunt",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2017-06-06", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("27ea8707d6d578e547037877"),
            "name": "Ad",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2020-07-31", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("5de4dbbcdbd74e7ff96e3f56"),
            "name": "Do",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2022-02-18", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("2c7771cd3d2915a2ae9bb3e3"),
            "name": "Ad",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2009-08-10", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("7d118129bd83a418f7c239c9"),
            "name": "Nostrud",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2019-02-27", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("e10a8c969147fff4e82f5b6f"),
            "name": "Do",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2019-02-03", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("6693b2d5f0f174c9b51e0c5b"),
            "name": "Voluptate",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2011-12-13", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("7a3f9bc5e51658da2e90a1a2"),
            "name": "Culpa",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2016-05-17", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("615987a393b01e3a2aaefa03"),
            "name": "Officia",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2020-06-11", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("7418628a9c443313a9a680f8"),
            "name": "Voluptate",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2015-09-15", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("93933ad17afcb9761dbd14c5"),
            "name": "Amet",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2011-09-22", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("7ce6776548462c3d1aa84668"),
            "name": "Aute",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2022-01-17", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("7e7539669a32a3da505bb6d6"),
            "name": "Ipsum",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2009-09-16", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("616c74fb77f05e008191302b"),
            "name": "Dolor",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2020-02-24", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("42420e110eb1f14e179dcb3e"),
            "name": "Officia",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2014-08-06", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("372adfd05b78d6ee37062f3f"),
            "name": "Proident",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2015-10-03", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("1869306d967c7d1710b18ab5"),
            "name": "Sint",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2015-12-21", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("9d0f1a2c79ad391e1426ff12"),
            "name": "Pariatur",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2017-12-14", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("86247ef3f23ba0edc47ba5fc"),
            "name": "Est",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2015-09-30", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("7d28156bd1786d59f658d32c"),
            "name": "Cupidatat",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2008-04-13", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("5b632ca21ea867d98e1a72d1"),
            "name": "Minim",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2015-07-01", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("86429f8fee63832b84dd4b01"),
            "name": "Occaecat",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2009-02-03", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("8b01154bac812c1c22fb253f"),
            "name": "Ea",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2010-04-05", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("967b1f1e3f3f515311c1b81b"),
            "name": "Ex",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2012-07-24", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("aef8a5993ede96c9186daff1"),
            "name": "Laboris",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2012-10-03", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("d5e77244f4cd71a00f971c97"),
            "name": "Do",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2018-08-17", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("2ed76bf61644739c92bced76"),
            "name": "Est",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2015-02-21", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("eaac55919cf89ee83ec532f1"),
            "name": "Duis",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2011-12-06", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("6dfab7d520510a204d791013"),
            "name": "Laborum",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2008-12-16", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("212538edb0ed73efd55105ff"),
            "name": "Sed",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2020-11-11", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("620409c24d2e44d84d17dd39"),
            "name": "Dolore",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2012-02-14", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("c0977c60a0b2ca0163a31b95"),
            "name": "Cillum",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2022-10-12", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("484cf698fd3d96e768c84276"),
            "name": "Sint",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2022-10-21", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("831c582a02df430bfed4cbcf"),
            "name": "Elit",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2014-10-12", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("db9034d1b3bae863b1909b02"),
            "name": "Nulla",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2017-09-05", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("2b93570a5e52763a946e2453"),
            "name": "Ut",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2018-04-16", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("9f0dbd92795514115b0e961a"),
            "name": "Excepteur",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2017-09-28", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("39b156ed1f80d16c177bb4e8"),
            "name": "Veniam",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2010-03-14", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("8574e9ccefc6251a83f3ec39"),
            "name": "Non",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2017-01-31", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("94a273cf26c954a2d15b6213"),
            "name": "Eu",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2014-09-30", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("c8b72d4a9393c0d489281b7b"),
            "name": "Exercitation",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2009-11-21", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("77811e19f91901060f595e5b"),
            "name": "Veniam",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2020-01-27", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("e8f62f60cf98a85102e1b23a"),
            "name": "Consectetur",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2019-01-04", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("730fe448ab25b716347ec828"),
            "name": "Eiusmod",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2017-11-29", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("8035b0c7e7b214288a157d20"),
            "name": "Laboris",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2016-11-25", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("5dac4eb727a46bdde37f27c8"),
            "name": "Aliquip",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2010-07-24", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("060640b1614ebbce99eb2b25"),
            "name": "Nulla",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2010-10-15", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("bcdd09e690698e702f96c18b"),
            "name": "Est",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2017-02-12", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("b4a7dc899d72e6954ec3aa28"),
            "name": "Sit",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2016-02-21", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("ab9cb7d5e02e0ef22859737a"),
            "name": "Sint",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2014-10-24", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("848fcd255ae646b623f8e79d"),
            "name": "Deserunt",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2016-07-28", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("8160bfeb8a32b070a8ccbb32"),
            "name": "Ea",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2020-06-29", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("dd191ded8dbb585f8109272a"),
            "name": "Labore",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2022-03-31", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("8c714825f536040f5d5a2474"),
            "name": "Adipiscing",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2019-10-26", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("8b95a7c7f07905e7ba100f47"),
            "name": "Qui",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2021-03-21", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("bb3e781b6717363785a65147"),
            "name": "Nostrud",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2021-07-20", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("284e8518f62cbaf6eeea36e9"),
            "name": "Nostrud",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2009-02-21", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("05df4ba254f0eeb21f20e980"),
            "name": "Cillum",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2015-10-01", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("65578f1a6232d48046a64b76"),
            "name": "Dolor",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2019-03-12", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("5326d07e1f9577fba0c6b333"),
            "name": "Reprehenderit",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2011-08-19", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("9e8794515f6b168c22fc14b1"),
            "name": "Ad",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2021-07-27", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("c4a1b823e06aff05df26e6c1"),
            "name": "In",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2016-10-28", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("a2243874b0c829097cec14ab"),
            "name": "Ad",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2013-06-20", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("78b1132f609ef3301eb73f9d"),
            "name": "Nostrud",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2016-12-09", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("3e4d9f009add3b4547932518"),
            "name": "Occaecat",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2009-05-03", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("044c1c8426bb31ad1ea90c94"),
            "name": "Esse",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2017-05-18", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("878e169419a3acec6492b492"),
            "name": "Sunt",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2015-03-12", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("df5071c5e768f1e6333dfdc4"),
            "name": "Ipsum",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2011-03-21", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("ec05279111912e0be6390a63"),
            "name": "Culpa",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2021-10-22", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("1731e21bea7ebd7ef0141a08"),
            "name": "Tempor",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2017-03-17", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("297c5f4399dca9cb93cc21c7"),
            "name": "Qui",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2017-10-31", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("6607ca0990ff6ecc2ed1d531"),
            "name": "Laboris",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2012-06-20", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("6fd93dd2116fcbd3a303ac41"),
            "name": "Et",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2016-07-19", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("76b2363c279b9eb73380088c"),
            "name": "Voluptate",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2022-02-27", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("0136797719bd484e632fc8d5"),
            "name": "Mollit",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2018-02-18", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("54276dabcb37255f3e0345e1"),
            "name": "Non",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2018-09-04", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("9e0f5f6a93304b466a6f24cb"),
            "name": "Ad",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2015-07-26", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("af1fa61ffbacd3690a681277"),
            "name": "Culpa",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2017-06-14", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("05a68fc915d7bdc187b0f1aa"),
            "name": "Laboris",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2011-03-17", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("a1d382b8ce3f1d32c61aba16"),
            "name": "Irure",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2020-06-20", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("b69e90022f199064d3609c1c"),
            "name": "Eu",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2017-06-14", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("817a216a24337e232701278a"),
            "name": "In",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2015-02-23", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("c6748148b0c61ffc2aec36d4"),
            "name": "Aliqua",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2009-03-17", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("e70d84f5db42449dab79615a"),
            "name": "Lorem",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2012-10-01", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("747b275ff008104b60080c16"),
            "name": "Cupidatat",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2014-11-03", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("b3ec43900402f87dad94a22d"),
            "name": "Velit",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2019-09-15", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("93a02d2cc186ef98fa3fa62b"),
            "name": "Occaecat",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2015-05-11", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("5d44b8e8c8ce1540b6a5c181"),
            "name": "Velit",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2010-04-11", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("d12baf99b78820b14a1af5b9"),
            "name": "Aute",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2010-05-28", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("8ef494fa6512c42e8115c6e6"),
            "name": "Aliqua",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2013-09-06", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("ea91f0576bbfb361bddcb06d"),
            "name": "Pariatur",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2012-10-08", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("9703eed1570e5de6ea3f231d"),
            "name": "Consectetur",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2020-03-16", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("5cbbb0fe7ffb67c7b9cdeb98"),
            "name": "Laborum",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2015-02-23", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("5ef744995a7f8bb9018d81ed"),
            "name": "Irure",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2014-04-14", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("b735bed8f636bfc2054bf685"),
            "name": "Ex",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2018-02-03", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("92e73bb7e8fbe1fd336afb67"),
            "name": "Esse",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2021-07-18", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("a9f7a973695792d72d4e07a3"),
            "name": "Proident",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2010-05-22", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("63575311489607f43759715f"),
            "name": "Enim",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2021-09-13", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("ff9478486d450dbdb9f867c7"),
            "name": "Minim",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2009-11-29", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("3ba9c033a47495c969910b78"),
            "name": "Et",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2022-08-23", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("225a3c528d9cbc27336361c0"),
            "name": "Excepteur",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2018-09-21", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("dfc67ab01f5bab6cf62126c4"),
            "name": "Consectetur",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2014-09-24", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("0405eff2cca291663df3c8f4"),
            "name": "Laborum",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2012-11-10", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("1d91a5b4248f20a43693e01a"),
            "name": "Mollit",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2016-01-03", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("d4b9362c1ac05867354338d4"),
            "name": "Duis",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2019-02-23", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("4ff84d378abc88a875e336ed"),
            "name": "Sed",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2010-07-31", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("62ae447e730259c2a49950c8"),
            "name": "Nulla",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2013-10-18", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("26fdb618231f738a1c022d32"),
            "name": "Nostrud",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2010-02-23", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("c19228dc6ae708594466d93f"),
            "name": "Nulla",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2011-07-23", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("890bd257da8c3c73855fc165"),
            "name": "Eiusmod",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2022-05-31", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("c93044f007cd24eae749d104"),
            "name": "Aliqua",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2022-10-27", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("7ae863aeb46364834a16d9b4"),
            "name": "Labore",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2012-12-10", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("238872556d49a4605dbf2960"),
            "name": "Id",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2014-03-10", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("1fda385b6a9dc99b1f096ad7"),
            "name": "Lorem",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2012-09-28", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("45f50c65c8c0acf5832ed21b"),
            "name": "Dolore",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2011-11-26", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("1258904c58b8ecd6f39f64a5"),
            "name": "Nulla",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2022-06-18", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("dd0a884285ded2eb0c18da0d"),
            "name": "Tempor",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2020-04-22", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("0c593ca2b7985aba7a3b2c08"),
            "name": "Dolore",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2014-11-22", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("649d06eea7df38ea31dde07e"),
            "name": "Mollit",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2011-02-16", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("3bdc83799a51d692fd57227b"),
            "name": "Amet",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2011-01-12", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("7030280a7a429b376e6d21ce"),
            "name": "Pariatur",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2019-10-17", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("4fc2a909603fa0a43f54b57b"),
            "name": "Nisi",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2020-10-23", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("45f2a8d94f82f6f03ede14f2"),
            "name": "Reprehenderit",
            "tweets": 8,
            "creation_date": datetime.datetime.strptime("2008-09-15", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("f0e5106a71b83b7377dc409c"),
            "name": "Id",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2018-11-16", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("cd81380a824ba8167aff03b9"),
            "name": "Commodo",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2013-04-16", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("7b191be1ae5f565dedeb9e72"),
            "name": "Nostrud",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2013-12-09", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("9421e50cde1b524a1406e888"),
            "name": "Veniam",
            "tweets": 9,
            "creation_date": datetime.datetime.strptime("2017-06-01", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("fab2b6d60107a2331df1c50d"),
            "name": "Nisi",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2012-03-22", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("45063ad6f3ddf69c4591fd69"),
            "name": "Non",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2009-03-23", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("7773b33eb3a1bbddf2c752fc"),
            "name": "Ullamco",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2019-10-29", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("6eaaef6d3d2e5e2d18653bf8"),
            "name": "Consectetur",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2011-09-05", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("38cd857c8e96ec78c32319e7"),
            "name": "Minim",
            "tweets": 4,
            "creation_date": datetime.datetime.strptime("2008-08-16", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("f36315978d58e09c496feba1"),
            "name": "Cupidatat",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2009-12-31", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("622bc1e1bbd97d8918adbe21"),
            "name": "Tempor",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2011-12-21", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("636fff692137ddb341b006f1"),
            "name": "Ex",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2011-06-16", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("23c8d03e5820c12f0fed71af"),
            "name": "Excepteur",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2021-09-05", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("78ffa700fdb3892c0dfa3d6f"),
            "name": "Consectetur",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2014-01-27", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("323a96559655da3f49cc4e52"),
            "name": "Quis",
            "tweets": 5,
            "creation_date": datetime.datetime.strptime("2012-04-20", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("cb761e0e6d648af0386db936"),
            "name": "Aliqua",
            "tweets": 6,
            "creation_date": datetime.datetime.strptime("2015-10-26", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("30437d1e7da5a6bb5c798733"),
            "name": "Nisi",
            "tweets": 7,
            "creation_date": datetime.datetime.strptime("2015-02-08", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("26150ee27bc3f1d3b0a630a6"),
            "name": "Incididunt",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2009-03-19", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("0af4c7de2ec78c477ea3e353"),
            "name": "Proident",
            "tweets": 0,
            "creation_date": datetime.datetime.strptime("2014-04-04", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("25ad444a4cd9fddbf817d3eb"),
            "name": "Occaecat",
            "tweets": 3,
            "creation_date": datetime.datetime.strptime("2021-08-20", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("cd84f00ae1a105dd2c5c58ca"),
            "name": "Officia",
            "tweets": 1,
            "creation_date": datetime.datetime.strptime("2009-04-21", "%Y-%m-%d")
        },
        {
            "_id": ObjectId("5eb3f521cf63707b082b71c3"),
            "name": "Tempor",
            "tweets": 2,
            "creation_date": datetime.datetime.strptime("2012-09-10", "%Y-%m-%d")
        }
    ]
)

# Print the number of documents inserted
print(f"{len(result.inserted_ids)} documents were inserted into the 'TAG' collection.")