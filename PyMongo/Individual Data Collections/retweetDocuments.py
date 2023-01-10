from pymongo import MongoClient
from bson.objectid import ObjectId
import datetime

# Connects to online MongoDB cluster
client = MongoClient("mongodb+srv://<user>:<password>@<cluster>.mongodb.net/?retryWrites=true&w=majority")

# Uses database TWEETER
db = client["TWEETER"]

# Uses RETWEET collection
collection = db["RETWEET"]

# Insert the documents into the RETWEET collection
result = collection.insert_many(
    [
        {
            "_id": ObjectId("16a4479a027b4957d6ea6a7b"),
            "tweet_id": ObjectId("e8db33a2ae34dc267d898d70"),
            "retweet_id": ObjectId("d9b6aba3c95316cea4871c48")
        },
        {
            "_id": ObjectId("e1e641363279c4db3af7b28a"),
            "tweet_id": ObjectId("ef4c5e12cc2a51432268da70"),
            "retweet_id": ObjectId("76abd4c200a153babeb443ac")
        },
        {
            "_id": ObjectId("e346b22549e25f3e3c14e4bb"),
            "tweet_id": ObjectId("5cfc79d8eb18f5af84000477"),
            "retweet_id": ObjectId("6557a6dcb6ef08d6fa8e698a")
        },
        {
            "_id": ObjectId("5bd3bf1dbd34085cdfa0f74f"),
            "tweet_id": ObjectId("d1acf9620b655d8a6382d141"),
            "retweet_id": ObjectId("16d4c237eb683d8511336249")
        },
        {
            "_id": ObjectId("b8b5aa916acd04cfce93da1f"),
            "tweet_id": ObjectId("2040dad76403df681a1eed84"),
            "retweet_id": ObjectId("5d9721331d8617b2b73c1691")
        },
        {
            "_id": ObjectId("c98e3f4dd6423fc81d5ab0e6"),
            "tweet_id": ObjectId("f004f20832bf9516d2f78ec7"),
            "retweet_id": ObjectId("d9097949f70628ad7dea586b")
        },
        {
            "_id": ObjectId("b02869900a0aa5283e2bbaa9"),
            "tweet_id": ObjectId("964f052b6a8ee9dcabca6f10"),
            "retweet_id": ObjectId("17d6387ac7a7506d7a2429a8")
        },
        {
            "_id": ObjectId("165f7de2f2068455cdbeb1b6"),
            "tweet_id": ObjectId("6017c9ff51648a6afd3cd853"),
            "retweet_id": ObjectId("bab1d957799a58ebc91b1016")
        },
        {
            "_id": ObjectId("d7c8e5607cb0b7d767aa5e06"),
            "tweet_id": ObjectId("a0409a8e5c411074d74f8aec"),
            "retweet_id": ObjectId("eca7446a9e5087231105403f")
        },
        {
            "_id": ObjectId("8950929ac770df2f39b50be5"),
            "tweet_id": ObjectId("531e73fffeb85511b77daa65"),
            "retweet_id": ObjectId("9e7ac68d7c96036e24fa9657")
        },
        {
            "_id": ObjectId("93b9d0a5862852f5254880eb"),
            "tweet_id": ObjectId("4b8453f92da5ed22417199c2"),
            "retweet_id": ObjectId("7b5c9943a5ff9c6a028c213c")
        },
        {
            "_id": ObjectId("4571b25df30f33faed84eebd"),
            "tweet_id": ObjectId("d58b4636dcf646e4d4f7db59"),
            "retweet_id": ObjectId("8c2526124d3978bd89006f32")
        },
        {
            "_id": ObjectId("75253f745e00b06dd97580af"),
            "tweet_id": ObjectId("7d03aeefda4c08f44ed19350"),
            "retweet_id": ObjectId("33f30a4f4e49b4e9048b2e6a")
        },
        {
            "_id": ObjectId("eec226e4360bfe4e96e061ec"),
            "tweet_id": ObjectId("18d199beb3748f05ef43eed3"),
            "retweet_id": ObjectId("3ed4c9660700f43c41f35f19")
        },
        {
            "_id": ObjectId("66e6cf7949374a4e16df7950"),
            "tweet_id": ObjectId("82a6ab0ef20a7aa738c46fad"),
            "retweet_id": ObjectId("7393c72a17de2bc0dabf1097")
        },
        {
            "_id": ObjectId("6cceaa1f61d134b891725f32"),
            "tweet_id": ObjectId("635bb5b8d257be05462584aa"),
            "retweet_id": ObjectId("b43eddba61e5513a4e6e28bf")
        },
        {
            "_id": ObjectId("bb66365beb8cc0b552bb29d8"),
            "tweet_id": ObjectId("9abedcf02aba26eb2a82ab23"),
            "retweet_id": ObjectId("1e6315deecfd7031836b6b03")
        },
        {
            "_id": ObjectId("6fa5c3fcaa1f715d69667969"),
            "tweet_id": ObjectId("26eaa471a964b76379ad4453"),
            "retweet_id": ObjectId("b6da78206675c0579f6c642d")
        },
        {
            "_id": ObjectId("94bebb950cfbb23b3388d182"),
            "tweet_id": ObjectId("c26d4d6d75347341c0082aa2"),
            "retweet_id": ObjectId("7798043a1f238ab46e770d64")
        },
        {
            "_id": ObjectId("e5d718c1a0a233b693deb62b"),
            "tweet_id": ObjectId("8e0714f49e946d22eb439193"),
            "retweet_id": ObjectId("e486051a5e5a4cd4e66b50f2")
        },
        {
            "_id": ObjectId("201ffaefe589ed249b7bb456"),
            "tweet_id": ObjectId("c24221f86ccbb23f9f61f777"),
            "retweet_id": ObjectId("b3737dffe2b4205dadd5029b")
        },
        {
            "_id": ObjectId("5108a5ac11d30219c757cd8d"),
            "tweet_id": ObjectId("5eca14b5bd73a41b71a63c43"),
            "retweet_id": ObjectId("f4e6783d801e9a323cbfe4e0")
        },
        {
            "_id": ObjectId("34d95848146265e310e7cf7a"),
            "tweet_id": ObjectId("1922da525bc721661395ad97"),
            "retweet_id": ObjectId("1d8e86695ac2e6b4701b9c22")
        },
        {
            "_id": ObjectId("b786662787bca48e07120314"),
            "tweet_id": ObjectId("73cce32176cf13caf1be1b05"),
            "retweet_id": ObjectId("f864eb12f8b68a54345b7de7")
        },
        {
            "_id": ObjectId("4178b32f0453cbd821a33a43"),
            "tweet_id": ObjectId("ef799e7a2823ae15f75c843d"),
            "retweet_id": ObjectId("9cb0db3c7ac7ec61161d3ed9")
        },
        {
            "_id": ObjectId("572f422bd64e779133bf8253"),
            "tweet_id": ObjectId("5605059f95e79b443bff40f4"),
            "retweet_id": ObjectId("df6c1aa3b42f2d3082e51ce6")
        },
        {
            "_id": ObjectId("13fb02686eab066c2ad69ac3"),
            "tweet_id": ObjectId("b24d01dec6cbb89ccf8f4b39"),
            "retweet_id": ObjectId("6a2acb68ab69c3afd93ff992")
        },
        {
            "_id": ObjectId("9cebac6476dd20ca7dab35eb"),
            "tweet_id": ObjectId("0439b245119b3500b809476c"),
            "retweet_id": ObjectId("2b30a57c2d12a133e4edaeac")
        },
        {
            "_id": ObjectId("c76a248f4e9d25c038cdf72c"),
            "tweet_id": ObjectId("72381d23ea9802706a2e999b"),
            "retweet_id": ObjectId("34b47a42d14e67023c6931d3")
        },
        {
            "_id": ObjectId("c9d8cd6211234225ed3ef309"),
            "tweet_id": ObjectId("bdb7f98115ba08ec6c80097f"),
            "retweet_id": ObjectId("aabd6eb69e272ba048f31832")
        },
        {
            "_id": ObjectId("c01a7d848cbfde34998eeb37"),
            "tweet_id": ObjectId("c66a931c9c3e244017e3c046"),
            "retweet_id": ObjectId("d1299cd50dbef846e1411d7d")
        },
        {
            "_id": ObjectId("009cc2483ff17378522da14b"),
            "tweet_id": ObjectId("97c2e20c2a62a3862c59e085"),
            "retweet_id": ObjectId("997cc863f9adc7b1f2b3694f")
        },
        {
            "_id": ObjectId("17cb2c61ab587d0fa6af108b"),
            "tweet_id": ObjectId("079021201a53207c77dbc332"),
            "retweet_id": ObjectId("29a679faa8d743c12168e6f9")
        },
        {
            "_id": ObjectId("638e10d91773863896fab4ca"),
            "tweet_id": ObjectId("38ca2607ee1da687d7ee0349"),
            "retweet_id": ObjectId("c942dadfaf4cc85fc63236e3")
        },
        {
            "_id": ObjectId("dc31621486d27ab21b4ff91b"),
            "tweet_id": ObjectId("947925f478e46850175c4c29"),
            "retweet_id": ObjectId("4965d761b6ddf9156173a521")
        },
        {
            "_id": ObjectId("94c10a093ff8cc85586cddbd"),
            "tweet_id": ObjectId("f91fba1d28ff4aaa90f9090f"),
            "retweet_id": ObjectId("02589330a1d7ea6086862351")
        },
        {
            "_id": ObjectId("a3e28b92eef1dd2640af87be"),
            "tweet_id": ObjectId("e6b22822a5f57345255b7af2"),
            "retweet_id": ObjectId("dec7a476c3d7a1ba4eae7431")
        },
        {
            "_id": ObjectId("70676e1bde5eb6756a108b48"),
            "tweet_id": ObjectId("06c3411adefe5c74f9bbd85d"),
            "retweet_id": ObjectId("be1cb4c4478d08dfb0757a9d")
        },
        {
            "_id": ObjectId("fd48063bf95809179af512ba"),
            "tweet_id": ObjectId("74cb434268192fc480f683d6"),
            "retweet_id": ObjectId("b9368c337c96940992996b06")
        },
        {
            "_id": ObjectId("4645aefd84298ee946c351b7"),
            "tweet_id": ObjectId("b27e48d4a0d57a1a7729998e"),
            "retweet_id": ObjectId("47e2b311d11dd61c284fb9bd")
        },
        {
            "_id": ObjectId("def5d71b23cd72cc609308a7"),
            "tweet_id": ObjectId("93eddafec38d31add54f76c5"),
            "retweet_id": ObjectId("ed742709e12b1c51c11b3d0d")
        },
        {
            "_id": ObjectId("e0d8049b399aab4276e87f8b"),
            "tweet_id": ObjectId("017cf024eae2db73920e80d6"),
            "retweet_id": ObjectId("84ef9bfbc10e9f634e9e1356")
        },
        {
            "_id": ObjectId("72bf40f23ed603f571e6c510"),
            "tweet_id": ObjectId("9bcae949cccebbf3557c7002"),
            "retweet_id": ObjectId("170f5bc918ba75d03749e17d")
        },
        {
            "_id": ObjectId("b1d48b0bb4c78f5a0586c0a7"),
            "tweet_id": ObjectId("fe34b6bbeefa39278fbb92d5"),
            "retweet_id": ObjectId("c11ebb995f612c6d01cb29b1")
        },
        {
            "_id": ObjectId("e666d1ded3c37d43cf5e3a13"),
            "tweet_id": ObjectId("013012f725c84d30cf9b3dfc"),
            "retweet_id": ObjectId("9777b639ff949d9173ebd424")
        },
        {
            "_id": ObjectId("1341a69ae077f807a90ca97f"),
            "tweet_id": ObjectId("a58037d4442f744b9ec61e2e"),
            "retweet_id": ObjectId("9da5a94158f292c9f6e09388")
        },
        {
            "_id": ObjectId("7fa8b48e53cb3cf23415d150"),
            "tweet_id": ObjectId("7893e0d390d5bdf5ea1e26a0"),
            "retweet_id": ObjectId("ba9b9f1308c78ccbbc64fe07")
        },
        {
            "_id": ObjectId("d6bfbfcf97c0d238cd269381"),
            "tweet_id": ObjectId("7b1f55fb84c9e2dd341929ee"),
            "retweet_id": ObjectId("91ef78357cdc5274a774350b")
        },
        {
            "_id": ObjectId("6b2de0b13c632ad3948fbf73"),
            "tweet_id": ObjectId("831d0139a49e7af4237e9352"),
            "retweet_id": ObjectId("c0353bd57e5653c2cc071644")
        },
        {
            "_id": ObjectId("1aca8194ad389fa66e9476ce"),
            "tweet_id": ObjectId("c71298a6f58f5c79c9662c77"),
            "retweet_id": ObjectId("272279d002a9654a30eec2ce")
        },
        {
            "_id": ObjectId("36cbdae0365eb5db51120607"),
            "tweet_id": ObjectId("0c58e3c70ec810d0b29a0f27"),
            "retweet_id": ObjectId("29d4dacfdff2d62351266b8c")
        },
        {
            "_id": ObjectId("27aee63e9b48be195ee14e8e"),
            "tweet_id": ObjectId("63656fad48bb87db77a48abb"),
            "retweet_id": ObjectId("bc403ffd698b2929f65cb894")
        },
        {
            "_id": ObjectId("b778fb6fcff85085c63399f5"),
            "tweet_id": ObjectId("9ef78d25849d1ea46e4c1ca7"),
            "retweet_id": ObjectId("5894c4184739434134613a93")
        },
        {
            "_id": ObjectId("e0937878f66f9693c158a52d"),
            "tweet_id": ObjectId("42b1c1e977df2c174db00220"),
            "retweet_id": ObjectId("490f3f7f9060d8899bb82b8e")
        },
        {
            "_id": ObjectId("ad7640cd1e218ee6d409ef73"),
            "tweet_id": ObjectId("f3c7e382af4ee01c14d2e82a"),
            "retweet_id": ObjectId("dcbd7b1e81efb8cb52ff2db2")
        },
        {
            "_id": ObjectId("e8bd2483dc37a1d2e52cf1e3"),
            "tweet_id": ObjectId("dc28d794c27b7d04d6d2b465"),
            "retweet_id": ObjectId("a4a01ea371f663ae0ca7eca4")
        },
        {
            "_id": ObjectId("16ff66c482b7a52e2ee4daba"),
            "tweet_id": ObjectId("cd966c5d960e3c626bc20dcc"),
            "retweet_id": ObjectId("f1df9b098c3aeac6a2651b66")
        },
        {
            "_id": ObjectId("d218eb5eaf08d29b779a6cda"),
            "tweet_id": ObjectId("f8a4d491990a5fc6211a3a04"),
            "retweet_id": ObjectId("9444b02b23a479acff964e0d")
        },
        {
            "_id": ObjectId("d483f2685173fe6905230b4c"),
            "tweet_id": ObjectId("d27c7dbffc8baeb9dfd570d0"),
            "retweet_id": ObjectId("157daaa5bf869d961934f1d2")
        },
        {
            "_id": ObjectId("3b5ed58624b37f8491334dac"),
            "tweet_id": ObjectId("02068c63a7499054daab84b4"),
            "retweet_id": ObjectId("2e259d04763f602d2a7b2606")
        },
        {
            "_id": ObjectId("d4cebf0d82faa7d11f4aeddc"),
            "tweet_id": ObjectId("eb001378bc5b0c116129598f"),
            "retweet_id": ObjectId("7dfbd709b69d10d40c17a8ac")
        },
        {
            "_id": ObjectId("743cc7f560bc27e125644a34"),
            "tweet_id": ObjectId("5331898dcaf0aa665556768f"),
            "retweet_id": ObjectId("e36e1d55c897cec6ccf2d885")
        },
        {
            "_id": ObjectId("4c2857ef5ca9e34d325e1563"),
            "tweet_id": ObjectId("a804a44c9a67e93c076e96e8"),
            "retweet_id": ObjectId("bab1d957799a58ebc91b1016")
        },
        {
            "_id": ObjectId("db3d89c76f332f94c03431db"),
            "tweet_id": ObjectId("b57e6b8993ac26ca4c8a88a3"),
            "retweet_id": ObjectId("5178261cba9c4586484d1e6d")
        },
        {
            "_id": ObjectId("e3045a36f164ac87805ca0b1"),
            "tweet_id": ObjectId("c5cd59b5cd2b6f36e78842dd"),
            "retweet_id": ObjectId("f517b4fef32afb2396fa73e9")
        },
        {
            "_id": ObjectId("2adcb92a2cf45b6f85bf5a88"),
            "tweet_id": ObjectId("78f1af1d1b32fcf238084e92"),
            "retweet_id": ObjectId("bee1e3766684037c0c2ee0a0")
        },
        {
            "_id": ObjectId("ea9f6788c930be66757d1323"),
            "tweet_id": ObjectId("8f2f995f89be66865710144f"),
            "retweet_id": ObjectId("762efba821c50cd47c870639")
        },
        {
            "_id": ObjectId("1f3ad52007a1c4829933484f"),
            "tweet_id": ObjectId("781cf8a90f49e6dc636aaca9"),
            "retweet_id": ObjectId("6d0abc4242146381033e3121")
        },
        {
            "_id": ObjectId("fab4657e50094d7cc7a42cbd"),
            "tweet_id": ObjectId("a73ee87f7d307c7362143ada"),
            "retweet_id": ObjectId("c80fe5515a41f2fd134eb4d8")
        },
        {
            "_id": ObjectId("2fc3e3b02e1c664c7d84f016"),
            "tweet_id": ObjectId("71fd851f3594e99c84753ae1"),
            "retweet_id": ObjectId("29c33bf243004375b7b071d4")
        },
        {
            "_id": ObjectId("1dc2903c70bd4de3bc3ac959"),
            "tweet_id": ObjectId("dc0eebe8435081a1adac6958"),
            "retweet_id": ObjectId("517241743fcbfe7ac6147ab0")
        },
        {
            "_id": ObjectId("d2476c5b7b7cf78bde79f1c7"),
            "tweet_id": ObjectId("b7ad63c9cec1884a8e1d35ec"),
            "retweet_id": ObjectId("78ea7a4ad7477dc289019fc5")
        },
        {
            "_id": ObjectId("49eb53e3d0633fc8c5be1c1e"),
            "tweet_id": ObjectId("1c8a6214e3569219e4a0763c"),
            "retweet_id": ObjectId("1c1462eca3741db9b467e34d")
        },
        {
            "_id": ObjectId("cd1bae812eb9741963a83312"),
            "tweet_id": ObjectId("47af1dac60b367f7e7b9c173"),
            "retweet_id": ObjectId("d8c701d5d6572c8637909803")
        },
        {
            "_id": ObjectId("f473923739c567f3c91d315b"),
            "tweet_id": ObjectId("7d4321e426129e3ae74014df"),
            "retweet_id": ObjectId("947925f478e46850175c4c29")
        },
        {
            "_id": ObjectId("9e2564266279c3d511e3d019"),
            "tweet_id": ObjectId("dc594ba96055acad9b6e0a1f"),
            "retweet_id": ObjectId("e844963413dab901b435a31e")
        },
        {
            "_id": ObjectId("bc3fe1479aa8fbc15f8641af"),
            "tweet_id": ObjectId("809cedb5fe8ec244ee9944ab"),
            "retweet_id": ObjectId("f5dee8f53fbf68d183a7ef52")
        },
        {
            "_id": ObjectId("76bf5b983e26ab0ec5d4d4a3"),
            "tweet_id": ObjectId("a6b63df180942a4212bdda03"),
            "retweet_id": ObjectId("18c8eccda0ffd56b4849fb1c")
        },
        {
            "_id": ObjectId("53084216405caa19fe5f6cee"),
            "tweet_id": ObjectId("015c17a5f4851e2a9b781fdd"),
            "retweet_id": ObjectId("63b19b50fa0eb279893b2305")
        },
        {
            "_id": ObjectId("9e49dc80041266485eafbfc1"),
            "tweet_id": ObjectId("8795779950eeb13016c7c821"),
            "retweet_id": ObjectId("5f83ebb86ff608be04fc2e46")
        },
        {
            "_id": ObjectId("8dfdfb616f80fe0a9f05b5cb"),
            "tweet_id": ObjectId("df243bb6b782690b2227f583"),
            "retweet_id": ObjectId("21a0c5299bb4adc2d5df3b9d")
        },
        {
            "_id": ObjectId("52de9b0380b0c9bd6e9479c6"),
            "tweet_id": ObjectId("9a50f606509b90553cf12aee"),
            "retweet_id": ObjectId("d686c55e3c847153096550d7")
        },
        {
            "_id": ObjectId("cfc1b7c3ab30a761f69b4628"),
            "tweet_id": ObjectId("9aab959fd2ff4937d0f29d78"),
            "retweet_id": ObjectId("e80dc3d7d8ef1174ddbbfdb1")
        },
        {
            "_id": ObjectId("b3654535e2950343ca7a6e8e"),
            "tweet_id": ObjectId("facb144813abf723dddeabf7"),
            "retweet_id": ObjectId("e9c5955b9f07c565055bec13")
        },
        {
            "_id": ObjectId("ecc3dbec6c4be2d58ebedadd"),
            "tweet_id": ObjectId("686138b672b072c1b2b45f5b"),
            "retweet_id": ObjectId("f3421ae1a77c8b3f1401bdf0")
        },
        {
            "_id": ObjectId("7b12e90e8ce2ee0398996df7"),
            "tweet_id": ObjectId("ec6ac95f1c7454e9991b08c9"),
            "retweet_id": ObjectId("b97ebd1f4f2d2f2ccf01c2f3")
        },
        {
            "_id": ObjectId("edbf904349eb68bdee7674b0"),
            "tweet_id": ObjectId("057daddd04942202b28dc949"),
            "retweet_id": ObjectId("2b326a4a8fd0ed1df585a9b8")
        },
        {
            "_id": ObjectId("103532e9085dad9904e56680"),
            "tweet_id": ObjectId("70ec44b35051db9cada13275"),
            "retweet_id": ObjectId("ed1c16af3bdccbf25a1c4994")
        },
        {
            "_id": ObjectId("c33547448d0f6b462d7bdf38"),
            "tweet_id": ObjectId("dad897adc62517241ee3d2dc"),
            "retweet_id": ObjectId("e6b9e0a122296d6be5f7d7ea")
        },
        {
            "_id": ObjectId("9b4326423aa5f406d8ae4f6c"),
            "tweet_id": ObjectId("0925d550c47c51e261e63991"),
            "retweet_id": ObjectId("db08f60c562e1027a3874133")
        },
        {
            "_id": ObjectId("45430f096cd9c08a390658b3"),
            "tweet_id": ObjectId("ac8d69682be062b5dfb81936"),
            "retweet_id": ObjectId("865e58c3780a58da10d18bf8")
        },
        {
            "_id": ObjectId("3d8eff5a0e5c98d12077efc2"),
            "tweet_id": ObjectId("2ba236916481c054f71aab9d"),
            "retweet_id": ObjectId("958088a553f1853e4c7a86a7")
        },
        {
            "_id": ObjectId("409c7d1e88e511570bd7f7ad"),
            "tweet_id": ObjectId("bf839ce553720c547dec2d42"),
            "retweet_id": ObjectId("188d2a3a8719d6e34e495177")
        },
        {
            "_id": ObjectId("1ea7bd09a9051e618ac64a13"),
            "tweet_id": ObjectId("2952f787b5a93ac888c2bdf0"),
            "retweet_id": ObjectId("cbf36e6d161faae81d5e9520")
        },
        {
            "_id": ObjectId("508cbffcc1ba16945631e22e"),
            "tweet_id": ObjectId("8eaadcb506142740346ef0f1"),
            "retweet_id": ObjectId("3ca92d968dc5098a4c13879e")
        },
        {
            "_id": ObjectId("46a8a1e90e98e9e3da7dc3d4"),
            "tweet_id": ObjectId("b35081edb4356a5d0193718f"),
            "retweet_id": ObjectId("0b9326acedf67dcc9245b191")
        },
        {
            "_id": ObjectId("651ccf278f02d3fa4120087e"),
            "tweet_id": ObjectId("3b38a6f983965efefb006f35"),
            "retweet_id": ObjectId("8343dcb98b61c31c1baa440a")
        },
        {
            "_id": ObjectId("c190164329345273d2228712"),
            "tweet_id": ObjectId("c9ea508b3788881199130430"),
            "retweet_id": ObjectId("7ef42c699a9489f42c666d05")
        },
        {
            "_id": ObjectId("a600e4a21a7bd9534e3bfa24"),
            "tweet_id": ObjectId("a552690caeaff779aae07b61"),
            "retweet_id": ObjectId("6907f267368e1be43fc80146")
        },
        {
            "_id": ObjectId("da8d2def52b9317cc8e8dd6e"),
            "tweet_id": ObjectId("b523d9b14cdbe04a7c21fc82"),
            "retweet_id": ObjectId("dadc20bc2f91ec8231a7d3bb")
        },
        {
            "_id": ObjectId("ad6e01619acdda8f702bf1ce"),
            "tweet_id": ObjectId("b3ea8caff4bf398f8822744f"),
            "retweet_id": ObjectId("f87f459bab6e1f688047cbdf")
        },
        {
            "_id": ObjectId("ad9bcd3362e653851f1a04fa"),
            "tweet_id": ObjectId("f333afca2ca1a264706c2d99"),
            "retweet_id": ObjectId("bb6568845218edf9d9f862fb")
        },
        {
            "_id": ObjectId("701e28fb4d40b831c7daa9f1"),
            "tweet_id": ObjectId("68e4cb7ebcc668a4c222f697"),
            "retweet_id": ObjectId("be0727a1a41e1e2d5af814dd")
        },
        {
            "_id": ObjectId("d3f6cd5540632f12d1b01300"),
            "tweet_id": ObjectId("7f68cabdb65582fdb58db0bc"),
            "retweet_id": ObjectId("99c2cf3803f5f0158d4fc031")
        },
        {
            "_id": ObjectId("a47ce4a1b048e86d923b666e"),
            "tweet_id": ObjectId("50e146ad5a860d2a59e3e846"),
            "retweet_id": ObjectId("94df469795df666cb8425d44")
        },
        {
            "_id": ObjectId("b69d3e6d9ebdc0cd32ea6a66"),
            "tweet_id": ObjectId("3d40570c059a32ea9b3d8c05"),
            "retweet_id": ObjectId("e21aef860fc866513bd979d7")
        },
        {
            "_id": ObjectId("07ca6f95d275c1674c472aa2"),
            "tweet_id": ObjectId("80a27de0be874cd07090c0df"),
            "retweet_id": ObjectId("6cddcce3ede2f857f61f6d76")
        },
        {
            "_id": ObjectId("a504000e69a3cc7d7cc5974b"),
            "tweet_id": ObjectId("2040dad76403df681a1eed84"),
            "retweet_id": ObjectId("076f602cfec64955501056a8")
        },
        {
            "_id": ObjectId("b0995d071c611da73550101f"),
            "tweet_id": ObjectId("779592060ae73b60a5384d42"),
            "retweet_id": ObjectId("7e4fa76e89a65c5afffb36aa")
        },
        {
            "_id": ObjectId("6bc78f43ced1ea0221d19f14"),
            "tweet_id": ObjectId("c9f0f58e2ff0fd9ec96d89ad"),
            "retweet_id": ObjectId("904deb0d537c582f38c5c174")
        },
        {
            "_id": ObjectId("b60d519aaa20fdde1dfacbfe"),
            "tweet_id": ObjectId("cb006608ba4f97d9b1341478"),
            "retweet_id": ObjectId("68a29eea189190c77b228f6a")
        },
        {
            "_id": ObjectId("355676a5be63d00b2aa1f7ac"),
            "tweet_id": ObjectId("10f160044c74259ff5fa2c89"),
            "retweet_id": ObjectId("f88e94295e5edb237db0caa7")
        },
        {
            "_id": ObjectId("32ba9ac2271a0366167c29cc"),
            "tweet_id": ObjectId("1dafe772590df729ac8ddcfe"),
            "retweet_id": ObjectId("f91fba1d28ff4aaa90f9090f")
        },
        {
            "_id": ObjectId("9746311dab361f2f1d0c4244"),
            "tweet_id": ObjectId("37ee67c82319df03f94086d1"),
            "retweet_id": ObjectId("3c6aff0ca5d85387cdc42499")
        },
        {
            "_id": ObjectId("2208b2477069c8d2e6e6a859"),
            "tweet_id": ObjectId("de11168d6cbbbbf8a142cbb4"),
            "retweet_id": ObjectId("483ebcedbbea68eef7db3b3c")
        },
        {
            "_id": ObjectId("123ecd35f6e63ff849603827"),
            "tweet_id": ObjectId("d7a5d78931a2e798da10da06"),
            "retweet_id": ObjectId("0c38497c0d7ba42475661099")
        },
        {
            "_id": ObjectId("ea16e838c1e0d0dd8e57c4db"),
            "tweet_id": ObjectId("a67970bd70708c9a126b47ca"),
            "retweet_id": ObjectId("76d2bd9318f891fccb2ea6e7")
        },
        {
            "_id": ObjectId("d6ab89ffa34000a0ead1ab48"),
            "tweet_id": ObjectId("2e9a95774a336d407610454c"),
            "retweet_id": ObjectId("2248e0d64ff097677a02e355")
        },
        {
            "_id": ObjectId("1b7a1aef26102f7dbf2f6284"),
            "tweet_id": ObjectId("f60c836691d02593d311d987"),
            "retweet_id": ObjectId("e12ceaf06656609274870262")
        },
        {
            "_id": ObjectId("c42c3dd8416cdd26da25110d"),
            "tweet_id": ObjectId("81d27569224f6bb1235af7eb"),
            "retweet_id": ObjectId("b7d0bd669f393eeecd58145c")
        },
        {
            "_id": ObjectId("3daee8017545df230488e4fc"),
            "tweet_id": ObjectId("e5de817f02ef56c54b4095e5"),
            "retweet_id": ObjectId("4d53f7f0ce148189c7f82d27")
        },
        {
            "_id": ObjectId("3ff7ac917cf884903637f933"),
            "tweet_id": ObjectId("f441cf1abc2cea2d8b1c769d"),
            "retweet_id": ObjectId("59a6b52d65e0522d6471aadd")
        },
        {
            "_id": ObjectId("a84574396d7dd542b6172187"),
            "tweet_id": ObjectId("1de95a3520b63c130ede3e5d"),
            "retweet_id": ObjectId("d9ac37850b8a6f1f1864555d")
        },
        {
            "_id": ObjectId("48bcd5041089928784857fce"),
            "tweet_id": ObjectId("b9ec3a0255ccebc99415af6d"),
            "retweet_id": ObjectId("4fe4d72e4a6982106d046d0a")
        },
        {
            "_id": ObjectId("336a08496cd4e8c58fd3e623"),
            "tweet_id": ObjectId("7dda61dbbf223435730b57f1"),
            "retweet_id": ObjectId("5a89ab3ab976a79745db4d54")
        },
        {
            "_id": ObjectId("2f015278688eeeebadcb6d4b"),
            "tweet_id": ObjectId("15e7a0678c86a5fa82066630"),
            "retweet_id": ObjectId("89e77dc3f053407d14f88cea")
        },
        {
            "_id": ObjectId("09bd64cf6bf3e62a362a14d2"),
            "tweet_id": ObjectId("546e7a20c7e6fa47adb5ca7f"),
            "retweet_id": ObjectId("170f5bc918ba75d03749e17d")
        },
        {
            "_id": ObjectId("18233a4b3557fc4fb0ebdd91"),
            "tweet_id": ObjectId("d405266c8b2b037747cdfb94"),
            "retweet_id": ObjectId("965d5d4fe1105c4f618c8d14")
        },
        {
            "_id": ObjectId("19461d2f31f9dfd8a2421888"),
            "tweet_id": ObjectId("3e5283ff8f5a0198d322d631"),
            "retweet_id": ObjectId("f8084c88182c0ade964a7e7c")
        },
        {
            "_id": ObjectId("2004158a38a92f8d70e66147"),
            "tweet_id": ObjectId("a12b40ca79350fd864bbf3f3"),
            "retweet_id": ObjectId("49d95c94d8a365c4bcd5cbb5")
        },
        {
            "_id": ObjectId("54f7b87b0fb95163e624f4c2"),
            "tweet_id": ObjectId("bb519835b93e37efe8fddbfe"),
            "retweet_id": ObjectId("955b4d23a044e9079e3561c8")
        },
        {
            "_id": ObjectId("d8ded8db4e5bd895b21a4c23"),
            "tweet_id": ObjectId("65322ffbac2aadacbdb16512"),
            "retweet_id": ObjectId("4dad985abe2c16abaef8810f")
        },
        {
            "_id": ObjectId("7372623d08e758c26ee49bf8"),
            "tweet_id": ObjectId("5b23d88e59e2589d9a60e6e1"),
            "retweet_id": ObjectId("a48d9abbe1de28c8c3ab8e12")
        },
        {
            "_id": ObjectId("6ddf7c57effb1d787d56a4fe"),
            "tweet_id": ObjectId("9d3fd0192d203069ec7dcc68"),
            "retweet_id": ObjectId("067e7e5ad8f383732061bf57")
        },
        {
            "_id": ObjectId("fe6288299a45d2f49272d982"),
            "tweet_id": ObjectId("d33506fe4a0881ff1dd456fd"),
            "retweet_id": ObjectId("f97a315451ef5dd8ba568050")
        },
        {
            "_id": ObjectId("670f228e2a75048c99b0f896"),
            "tweet_id": ObjectId("335bb1a26e8f547b9a21fa70"),
            "retweet_id": ObjectId("542d0d6ad7cd92c6c898a967")
        },
        {
            "_id": ObjectId("25ec53b8ce8089c1b421802b"),
            "tweet_id": ObjectId("e4724a54133f9a32fb034f47"),
            "retweet_id": ObjectId("9e438228f0bbad8ab5ed91cc")
        },
        {
            "_id": ObjectId("b439f357309829e2706a19ab"),
            "tweet_id": ObjectId("a6e312055bc9463a2f64ca11"),
            "retweet_id": ObjectId("478001fc450c5d2c3d987fd1")
        },
        {
            "_id": ObjectId("6906152089c0a8dd0298d704"),
            "tweet_id": ObjectId("81eaae6782265bcd7e7d86a4"),
            "retweet_id": ObjectId("34338ea189fcfe7f2aa9ff97")
        },
        {
            "_id": ObjectId("242153dac3782bb1df354eaa"),
            "tweet_id": ObjectId("5a89ab3ab976a79745db4d54"),
            "retweet_id": ObjectId("6fe91ca9baa40f2665aa57ea")
        },
        {
            "_id": ObjectId("55c7d76f16dc94c8e3620ce7"),
            "tweet_id": ObjectId("61b8e24c757b48f4c252b137"),
            "retweet_id": ObjectId("4c9f2da91562ee9cc3799d54")
        },
        {
            "_id": ObjectId("8c11e56a98774804a099d8bd"),
            "tweet_id": ObjectId("b6f30457a4bbc6be8f8cea35"),
            "retweet_id": ObjectId("047389cb9e320d5716c05781")
        },
        {
            "_id": ObjectId("998e6a1dbb35de3eafb10826"),
            "tweet_id": ObjectId("badeef6d845295133db8193a"),
            "retweet_id": ObjectId("7e5b8a86a7ce776428aeefda")
        },
        {
            "_id": ObjectId("962c469764c9bb3055edb8f0"),
            "tweet_id": ObjectId("b6ff0f2d3ee054e25fe2672f"),
            "retweet_id": ObjectId("27377eb2c65b8508e6fdde28")
        },
        {
            "_id": ObjectId("83d2f9cba4f9eca496f72585"),
            "tweet_id": ObjectId("bc6e4e878f20a1a80ef11fe0"),
            "retweet_id": ObjectId("62d773fedcb0074a6f9b802f")
        },
        {
            "_id": ObjectId("f590dfc286a22d28edbcd2e7"),
            "tweet_id": ObjectId("f0c257959f93c606569c80cf"),
            "retweet_id": ObjectId("87c228ac85aa5b00bebf748e")
        },
        {
            "_id": ObjectId("873b44ca5cda2f18fd4d7576"),
            "tweet_id": ObjectId("8b64b2b5dfe295981d7f6fe0"),
            "retweet_id": ObjectId("e4188134e128846da3a5cd55")
        },
        {
            "_id": ObjectId("92a5339e4a177835f0e93d3f"),
            "tweet_id": ObjectId("8b41278f00ab768dd30df7e3"),
            "retweet_id": ObjectId("6f2814363b98fab695c5800f")
        },
        {
            "_id": ObjectId("25f091164be4abd6eca34fa5"),
            "tweet_id": ObjectId("98ba4f72e63a2399a27ea3e8"),
            "retweet_id": ObjectId("13a024fac8b4e6f8e98c8876")
        },
        {
            "_id": ObjectId("c760ed4c9a25c16126887a24"),
            "tweet_id": ObjectId("a2f193ff7aa9b18a076c13bd"),
            "retweet_id": ObjectId("34f9d1b9b5260b664b5d273e")
        },
        {
            "_id": ObjectId("44e6de8bb7a311fe3864a422"),
            "tweet_id": ObjectId("e3e453386beaf49c87d8b5c7"),
            "retweet_id": ObjectId("3acc3032bb12de6e1fe4114d")
        },
        {
            "_id": ObjectId("b140bd6a360a809e8cdfae13"),
            "tweet_id": ObjectId("a4e3ff19f57e55c396cfe525"),
            "retweet_id": ObjectId("3825dc60d0812ded400c546d")
        },
        {
            "_id": ObjectId("f99f1a17e82440bf968f2a61"),
            "tweet_id": ObjectId("a2db61ccfd4b12b4d7be054f"),
            "retweet_id": ObjectId("0bb77cda52a0a875efc39307")
        },
        {
            "_id": ObjectId("c1f0f1ae570cb180fdccb8de"),
            "tweet_id": ObjectId("5b9070cf1dd571fd18e37278"),
            "retweet_id": ObjectId("dd2a109fb2a4a7d7061dabbc")
        },
        {
            "_id": ObjectId("356cb35818e99c8b059ded02"),
            "tweet_id": ObjectId("6f9a1ec94fa600a05fde5cb0"),
            "retweet_id": ObjectId("ee38e11863f80f4455ded0a9")
        },
        {
            "_id": ObjectId("793ddff030a6745de969fe52"),
            "tweet_id": ObjectId("02323238ce17ee785dd500fa"),
            "retweet_id": ObjectId("500413b9a60eaec2c999c33c")
        },
        {
            "_id": ObjectId("76d3ea62e0b46b53f54d1546"),
            "tweet_id": ObjectId("f7b977273729a6d030d7d908"),
            "retweet_id": ObjectId("623d4ff13979713b5d2051fc")
        },
        {
            "_id": ObjectId("6abb516d51b4002fc3a3f1d8"),
            "tweet_id": ObjectId("eb8bdd01a0ddb00435e8a805"),
            "retweet_id": ObjectId("3656af847a9524f007b5a8e1")
        },
        {
            "_id": ObjectId("20f96f4e25f625d8e7ea6a38"),
            "tweet_id": ObjectId("d1cd97b07f1070fd86901e3d"),
            "retweet_id": ObjectId("df6c1aa3b42f2d3082e51ce6")
        },
        {
            "_id": ObjectId("8801cc1ee9a59e83630aceec"),
            "tweet_id": ObjectId("cae333551a587abf627889e8"),
            "retweet_id": ObjectId("79b5f56bed7e2b40d7d3355c")
        },
        {
            "_id": ObjectId("07a2c0cf3cf5391bb09e773b"),
            "tweet_id": ObjectId("829c194092b64ca468b6f559"),
            "retweet_id": ObjectId("c44e0b326f4c5cd08d1ff159")
        },
        {
            "_id": ObjectId("58d03468935d0daa6bc5053e"),
            "tweet_id": ObjectId("b3c09f439b83a76762f32aa3"),
            "retweet_id": ObjectId("1ca22dd33a8a88181c97343c")
        },
        {
            "_id": ObjectId("f4a20fd8aff261205b18f62f"),
            "tweet_id": ObjectId("92b9dc7849511040b6c5231b"),
            "retweet_id": ObjectId("b92ebdc83bdb11d7f4cc35b3")
        },
        {
            "_id": ObjectId("5418fd38f66c5a9b85782cb8"),
            "tweet_id": ObjectId("98ba4f72e63a2399a27ea3e8"),
            "retweet_id": ObjectId("c7351f4093d04f2ad31c8a02")
        },
        {
            "_id": ObjectId("a2b16d433fcfd3a477615d11"),
            "tweet_id": ObjectId("26752d1d708c0e6ba6fe7116"),
            "retweet_id": ObjectId("bb97d5a70eabdd52bc2f21c6")
        },
        {
            "_id": ObjectId("25c4cea5c2091727b1a7e6b2"),
            "tweet_id": ObjectId("65322ffbac2aadacbdb16512"),
            "retweet_id": ObjectId("f5ce83049244e9c1887ee5e5")
        },
        {
            "_id": ObjectId("9bb2d7d39997219d7a71a708"),
            "tweet_id": ObjectId("83ddfeb59cd3502a2ccbd824"),
            "retweet_id": ObjectId("a5431166741d018e766cef6a")
        },
        {
            "_id": ObjectId("232d958d472afd830ef675b8"),
            "tweet_id": ObjectId("caf65a3ecdb23b6db75cfcb5"),
            "retweet_id": ObjectId("4cd83bf38d8f3def8b478eeb")
        },
        {
            "_id": ObjectId("55f50a5661fabec70de1c48f"),
            "tweet_id": ObjectId("6d7ba1409cf44c6669c1c409"),
            "retweet_id": ObjectId("fb6414274733fdae05aaa215")
        },
        {
            "_id": ObjectId("4805931ae39f40560e29f850"),
            "tweet_id": ObjectId("2d654fe20a88b07431129ca8"),
            "retweet_id": ObjectId("c70f2bcedc59a7cb58024a72")
        },
        {
            "_id": ObjectId("a0ad43815e8ccd1e7fccbcfc"),
            "tweet_id": ObjectId("615349f37e26864d65305a02"),
            "retweet_id": ObjectId("27fb8aec51e12fcdcbe7d647")
        },
        {
            "_id": ObjectId("f470f1b758cf4ed2edffd727"),
            "tweet_id": ObjectId("dd4426af53e4862c058f79b2"),
            "retweet_id": ObjectId("91b037905f31a50111c931ba")
        },
        {
            "_id": ObjectId("2c5b7d7332a31aa821bad60b"),
            "tweet_id": ObjectId("5a388f26d044cdd3570d5cff"),
            "retweet_id": ObjectId("76d7567cc065c6dcee4209fa")
        },
        {
            "_id": ObjectId("bd0aba289a9cdab38d03ab32"),
            "tweet_id": ObjectId("65875cf5be606ca318a05e0e"),
            "retweet_id": ObjectId("92a5d7986f95937d34af6a45")
        },
        {
            "_id": ObjectId("13cbfcc5f023f1ac88d5aa6d"),
            "tweet_id": ObjectId("aefbe95b5e295ff4621a4965"),
            "retweet_id": ObjectId("a5f815e480e4fb11bd49e4a5")
        },
        {
            "_id": ObjectId("e614cea082429f22c9b219ab"),
            "tweet_id": ObjectId("2e9a95774a336d407610454c"),
            "retweet_id": ObjectId("03c5261c090905c05d1c744e")
        },
        {
            "_id": ObjectId("f0426d7f9175b2d64364cd22"),
            "tweet_id": ObjectId("471863cdbd290fe3aef19df8"),
            "retweet_id": ObjectId("08b89b49c6962282bb818e31")
        },
        {
            "_id": ObjectId("9ca982acc73a31e71d549169"),
            "tweet_id": ObjectId("38f37a53bf7c90a67d1ebaea"),
            "retweet_id": ObjectId("a1e4c9c1cefd4f610f34ad1d")
        },
        {
            "_id": ObjectId("69cdb6bc361845fdb1316cd4"),
            "tweet_id": ObjectId("0e372d17125d8d4d0f2338cf"),
            "retweet_id": ObjectId("a44bf9a7ef6d069cd43f0f31")
        },
        {
            "_id": ObjectId("0093cab9838f53665a17f587"),
            "tweet_id": ObjectId("b118ede97bc7fb03d40b45ec"),
            "retweet_id": ObjectId("b51e273784f789f5e6f6cb82")
        },
        {
            "_id": ObjectId("01c5d235d964944043dacfec"),
            "tweet_id": ObjectId("67116ac9a5349da151feb7ed"),
            "retweet_id": ObjectId("9533badda6bda7a762b778af")
        },
        {
            "_id": ObjectId("e35a8c03be1fdb2bcf835c2d"),
            "tweet_id": ObjectId("8d4a8a799a492ead17684781"),
            "retweet_id": ObjectId("5a89ab3ab976a79745db4d54")
        },
        {
            "_id": ObjectId("ed45bd81464b6313a80650af"),
            "tweet_id": ObjectId("88a0604c6e0d9e2c0a061bd8"),
            "retweet_id": ObjectId("90d5ebf67fb7c90a7654b963")
        },
        {
            "_id": ObjectId("c9ce183f70bdb5139aa8c3ca"),
            "tweet_id": ObjectId("e23226d31f1b5311c9447613"),
            "retweet_id": ObjectId("f8daa24de8bbb7d5eb434288")
        },
        {
            "_id": ObjectId("bf80cd281e8dd23476b5210e"),
            "tweet_id": ObjectId("633565dad57b62ce2c98f18d"),
            "retweet_id": ObjectId("e3b41a7c60c6f31abb798eeb")
        },
        {
            "_id": ObjectId("8d4e36a9988ab8e317b25b5a"),
            "tweet_id": ObjectId("44d08f54304a401cc935b3de"),
            "retweet_id": ObjectId("c37c3cdfb444bd52312ba0ac")
        },
        {
            "_id": ObjectId("3a4895d4c8ac187bcfc3163d"),
            "tweet_id": ObjectId("fc607b2259b83468f425c585"),
            "retweet_id": ObjectId("afd5a139ebf129cbf06504ed")
        },
        {
            "_id": ObjectId("daf03bbb02a035b233ca4c9c"),
            "tweet_id": ObjectId("73f3572c0e3452f982eb08c0"),
            "retweet_id": ObjectId("8fad0cd3260f4dcb196cccd0")
        },
        {
            "_id": ObjectId("690950af2b8032053f245862"),
            "tweet_id": ObjectId("e23226d31f1b5311c9447613"),
            "retweet_id": ObjectId("2959f778ce4992d5b5fd3b82")
        },
        {
            "_id": ObjectId("6485b201caffc1d2b6a430bf"),
            "tweet_id": ObjectId("57eef963f0100e9bf7c64f6c"),
            "retweet_id": ObjectId("43331f01377f947b50b7e9c1")
        },
        {
            "_id": ObjectId("949a4bf3756704da0fe1c05c"),
            "tweet_id": ObjectId("26eaa471a964b76379ad4453"),
            "retweet_id": ObjectId("214f65969c9cb23ec0236ffc")
        },
        {
            "_id": ObjectId("595f79bbf23785e0f9398a9e"),
            "tweet_id": ObjectId("05905dafc44c23dff59d3934"),
            "retweet_id": ObjectId("cb3f76f1f9185a766bdf21a2")
        },
        {
            "_id": ObjectId("695f52c76dfe0720dcb3d6ea"),
            "tweet_id": ObjectId("44d08f54304a401cc935b3de"),
            "retweet_id": ObjectId("d56a58072cd4e5813327275c")
        },
        {
            "_id": ObjectId("8fb9725c3e13f7be7be0ef55"),
            "tweet_id": ObjectId("8e0e9da332a95c4d686a8a1f"),
            "retweet_id": ObjectId("b27e48d4a0d57a1a7729998e")
        },
        {
            "_id": ObjectId("6c51a35af476805750bb509a"),
            "tweet_id": ObjectId("170f5bc918ba75d03749e17d"),
            "retweet_id": ObjectId("1135fba11adf8a01046b689e")
        },
        {
            "_id": ObjectId("a57905b82857df8b8f0759a1"),
            "tweet_id": ObjectId("01ff929f2d151d4194246fef"),
            "retweet_id": ObjectId("dc28d794c27b7d04d6d2b465")
        },
        {
            "_id": ObjectId("a19dc0a94872babc1624d2bd"),
            "tweet_id": ObjectId("185a6b02b254067eb12b99db"),
            "retweet_id": ObjectId("cedff1399c0e41202bbc8f8c")
        },
        {
            "_id": ObjectId("45c50cad2197c6d95dea3bc4"),
            "tweet_id": ObjectId("920e1b4f4e99c6e4ea55b51d"),
            "retweet_id": ObjectId("d72a154c3c5c695662fe41e4")
        },
        {
            "_id": ObjectId("39d441cd0ba516dde0f23690"),
            "tweet_id": ObjectId("9e438228f0bbad8ab5ed91cc"),
            "retweet_id": ObjectId("967910f27ccffae027bcd079")
        },
        {
            "_id": ObjectId("fd220755464383b000edda8b"),
            "tweet_id": ObjectId("4197a73486602175972fb8d6"),
            "retweet_id": ObjectId("13e61c873201b388b5d64f95")
        },
        {
            "_id": ObjectId("a4cf03194dc63d238cd0b7e5"),
            "tweet_id": ObjectId("030adbc2dd73b54bee8b31cd"),
            "retweet_id": ObjectId("6ec2a7632e330b4a1e098af4")
        },
        {
            "_id": ObjectId("614ed49610e81dfd42ad2674"),
            "tweet_id": ObjectId("7e78c0ed5c87a1ca69f0e92d"),
            "retweet_id": ObjectId("878ffa0db11cd25e672fe0ce")
        },
        {
            "_id": ObjectId("560382c79b37fddd75142777"),
            "tweet_id": ObjectId("2e170253be520140956e449f"),
            "retweet_id": ObjectId("b231395ff358f649716acc1a")
        },
        {
            "_id": ObjectId("3ae4a65560f2fb2cf125dd07"),
            "tweet_id": ObjectId("ba88465e229a01cda2aae7dc"),
            "retweet_id": ObjectId("8a9221013652dca730743791")
        },
        {
            "_id": ObjectId("eb8ce979991642af9ee1ee73"),
            "tweet_id": ObjectId("28ece721448af85e63aa1662"),
            "retweet_id": ObjectId("2c201498a294ecb7c94c032f")
        },
        {
            "_id": ObjectId("e3d74ff225fb683c650f3547"),
            "tweet_id": ObjectId("692c66c0ea901aedfc444206"),
            "retweet_id": ObjectId("220d681ac8feb88f23a08fbf")
        },
        {
            "_id": ObjectId("1da0091c6766d4466c78f436"),
            "tweet_id": ObjectId("0d14f854897250e2957bb051"),
            "retweet_id": ObjectId("4e445ab8209d49d1feaa7971")
        },
        {
            "_id": ObjectId("57297ab0340af371bbdd4a69"),
            "tweet_id": ObjectId("da65ecf98ff79db4382185b6"),
            "retweet_id": ObjectId("30ed546cec1bf3877839c113")
        },
        {
            "_id": ObjectId("e9eebc5f8e4da6cf0f2c3df1"),
            "tweet_id": ObjectId("5c4fb1e9367dc350328d4da5"),
            "retweet_id": ObjectId("9f6ee670ef9b94fc79c68a12")
        },
        {
            "_id": ObjectId("e96445d91c2ab8da20367528"),
            "tweet_id": ObjectId("27251a04a46399c62ff4be75"),
            "retweet_id": ObjectId("39ce057b3d89c7d0133fd56a")
        },
        {
            "_id": ObjectId("dd8dff11314260760cf656bf"),
            "tweet_id": ObjectId("c6493fca331fd6285075a012"),
            "retweet_id": ObjectId("d3e2d50011bccb590599e523")
        },
        {
            "_id": ObjectId("d8227a65b81562fcbeaa481f"),
            "tweet_id": ObjectId("7ca8e70b2488eab89aea2502"),
            "retweet_id": ObjectId("d421264079640333714812e7")
        },
        {
            "_id": ObjectId("434d17831c650ad0fa88a329"),
            "tweet_id": ObjectId("8feb838c99382c564d751c13"),
            "retweet_id": ObjectId("5b66ec6d98e2dea4fa9655a1")
        },
        {
            "_id": ObjectId("c68e1703028e84a8e3cac58b"),
            "tweet_id": ObjectId("159302f16ab59c5c0db142be"),
            "retweet_id": ObjectId("6c2ba13e42226269f237b850")
        },
        {
            "_id": ObjectId("07acf9d70fd05a462827ad89"),
            "tweet_id": ObjectId("0d0807f076628789b333cfa2"),
            "retweet_id": ObjectId("0943828a8b2c03d821c8fd7b")
        },
        {
            "_id": ObjectId("65e4a2ca9b00cab0a665ab3a"),
            "tweet_id": ObjectId("9c58261cd4004d2889b44542"),
            "retweet_id": ObjectId("84c8ada9f4fcd6ad6b6b5d63")
        },
        {
            "_id": ObjectId("7003ce897af0638ca10e47eb"),
            "tweet_id": ObjectId("2c171dafe15bdb762f9238d6"),
            "retweet_id": ObjectId("1a7b0460a394f93afbc71342")
        },
        {
            "_id": ObjectId("1d4e8182077b7ee338ecc2de"),
            "tweet_id": ObjectId("32d6a94835e4e2799dd22a3f"),
            "retweet_id": ObjectId("16d2d4777307042945277d00")
        },
        {
            "_id": ObjectId("c3edb6f66ee54432d3258f04"),
            "tweet_id": ObjectId("be45a38896a8983a09b8cf8b"),
            "retweet_id": ObjectId("7cd6c6ea34b16ab7c1f5ff39")
        },
        {
            "_id": ObjectId("6c68778b9607fe0c2ed5f69c"),
            "tweet_id": ObjectId("838e79a79735134d693125a0"),
            "retweet_id": ObjectId("fa4cc2c8ef6f2d066314dba3")
        },
        {
            "_id": ObjectId("47e71727777772073fa0fff3"),
            "tweet_id": ObjectId("8a99271fbf747f4449d8cfca"),
            "retweet_id": ObjectId("4428990bbe876426fcb1b210")
        },
        {
            "_id": ObjectId("4892d32833fc94093f84e1e8"),
            "tweet_id": ObjectId("41f97a090a2e5029c6fd3d90"),
            "retweet_id": ObjectId("edf4dbd84b5acc1758c88867")
        },
        {
            "_id": ObjectId("229f0da44ad782e8df7eafe2"),
            "tweet_id": ObjectId("f9a66a9d2c9f8dc9fca34bf0"),
            "retweet_id": ObjectId("3e5283ff8f5a0198d322d631")
        },
        {
            "_id": ObjectId("1c19b80b11f7d2220cee9864"),
            "tweet_id": ObjectId("6912fd3a87aed0df71d278d4"),
            "retweet_id": ObjectId("f9d55273653c0b8576dfa1d4")
        },
        {
            "_id": ObjectId("bd9828cc2414bceb05549d51"),
            "tweet_id": ObjectId("584770a4d47d3c1d3c34385e"),
            "retweet_id": ObjectId("bf4fdcfca1fe197021129a48")
        },
        {
            "_id": ObjectId("734e27b4aa5c9370120eb9a9"),
            "tweet_id": ObjectId("eb525443ae0eab94e19f0391"),
            "retweet_id": ObjectId("632f467840568809ad25a33d")
        },
        {
            "_id": ObjectId("dbda6a664ad54ffd0706c2ec"),
            "tweet_id": ObjectId("576169d2cd4178ff11ad1252"),
            "retweet_id": ObjectId("abfd3b1b44b979f99449f984")
        },
        {
            "_id": ObjectId("cab803598ea18263b09826cc"),
            "tweet_id": ObjectId("b62364dd0ef06cd95d73b632"),
            "retweet_id": ObjectId("719a5f789d13ac8124732f9d")
        },
        {
            "_id": ObjectId("75d3fb1608704338431de394"),
            "tweet_id": ObjectId("014b5267dc2e025608d0a5bb"),
            "retweet_id": ObjectId("37e6be3d150084971945ed46")
        },
        {
            "_id": ObjectId("daa977982244dc4910811f59"),
            "tweet_id": ObjectId("d7a5d78931a2e798da10da06"),
            "retweet_id": ObjectId("dc594ba96055acad9b6e0a1f")
        },
        {
            "_id": ObjectId("d32801b4753139d741034ff3"),
            "tweet_id": ObjectId("44470ed7eae262e87a89078e"),
            "retweet_id": ObjectId("500ab09054a14d9f069478ee")
        },
        {
            "_id": ObjectId("77beed432bfbf713f0cd1fa2"),
            "tweet_id": ObjectId("eb9d5724e1bef7ba466de494"),
            "retweet_id": ObjectId("34bfe63526527dbc98d19f09")
        },
        {
            "_id": ObjectId("19df3c2653a0ecc234ec8e3c"),
            "tweet_id": ObjectId("9c450d7d5f139a336979461f"),
            "retweet_id": ObjectId("b756ffe44f8c8234a04494bb")
        },
        {
            "_id": ObjectId("063d33f87bd9fb3509292a9c"),
            "tweet_id": ObjectId("fd9553c5a82fedeb3a2ce0c5"),
            "retweet_id": ObjectId("157daaa5bf869d961934f1d2")
        },
        {
            "_id": ObjectId("52a2aea7664c8b93e9aaee83"),
            "tweet_id": ObjectId("794ed506636d2e788f2cf1d7"),
            "retweet_id": ObjectId("70f18edb525dce2bf9fdf761")
        },
        {
            "_id": ObjectId("71eb1db23d0b030ad6293a55"),
            "tweet_id": ObjectId("560cbb93e04bbe2172d82d34"),
            "retweet_id": ObjectId("7731593e312e766ca0d2d352")
        },
        {
            "_id": ObjectId("71ad6bbe4e59e3de1389869c"),
            "tweet_id": ObjectId("0a2658c0e1dc7951ada39b21"),
            "retweet_id": ObjectId("0f7e8cd79b58b90ac1c41b03")
        },
        {
            "_id": ObjectId("a4b8b6ff4aadddd708db86bc"),
            "tweet_id": ObjectId("a6452cccf1f310ae99008f5e"),
            "retweet_id": ObjectId("37ee67c82319df03f94086d1")
        },
        {
            "_id": ObjectId("60c04ab7f61e59836c5b19bf"),
            "tweet_id": ObjectId("c8eb5b61015d55855f11e206"),
            "retweet_id": ObjectId("6b337463206ffd2e60938a67")
        },
        {
            "_id": ObjectId("f0794b6334afe4eadd675e5d"),
            "tweet_id": ObjectId("c88c7c960ba213e57faca074"),
            "retweet_id": ObjectId("32e4da8f8f034a8b323937f4")
        },
        {
            "_id": ObjectId("aa614b5656b8557dfbc6de1e"),
            "tweet_id": ObjectId("2afdac65fb2d8d6aeaad84f6"),
            "retweet_id": ObjectId("0148d07468f5337b88397b4b")
        },
        {
            "_id": ObjectId("70a09dfba26ca4c593e12ac3"),
            "tweet_id": ObjectId("5b23d88e59e2589d9a60e6e1"),
            "retweet_id": ObjectId("7dd40fbbb41d28c516516afd")
        },
        {
            "_id": ObjectId("c9e6fef50e4c89e58c92e43c"),
            "tweet_id": ObjectId("c9f7c22c7e277128407d7afa"),
            "retweet_id": ObjectId("11ae1fedd561b4c2a26a40a0")
        },
        {
            "_id": ObjectId("09f319cc64ca44a62f3de7e9"),
            "tweet_id": ObjectId("08a3602f62be64c97754612e"),
            "retweet_id": ObjectId("acc5a3c307c62db9c1c520d7")
        },
        {
            "_id": ObjectId("eb80eda04b6758261b9cf668"),
            "tweet_id": ObjectId("b377e479a4a3769b89c55b01"),
            "retweet_id": ObjectId("a59f92b3ba05f7855179a83c")
        },
        {
            "_id": ObjectId("51e0a076d24e1793f32b3954"),
            "tweet_id": ObjectId("7937ba48e69922756fd5c939"),
            "retweet_id": ObjectId("5236d8bc4542703a102ac395")
        },
        {
            "_id": ObjectId("bcb90f5e8dbb878c569c7358"),
            "tweet_id": ObjectId("3fe11cb32840b5a1a2b0a35e"),
            "retweet_id": ObjectId("6da93bce7d9b2257b30ed34a")
        },
        {
            "_id": ObjectId("9625a0076068730a55caa6bf"),
            "tweet_id": ObjectId("fa886dda32c273cf62bee90c"),
            "retweet_id": ObjectId("dcf37878283625dc010fe5fa")
        },
        {
            "_id": ObjectId("aa6217d1c5945d7010e73117"),
            "tweet_id": ObjectId("8e48f3d2df0a808382823e0f"),
            "retweet_id": ObjectId("bc41c2ee7814cfb5cd302712")
        },
        {
            "_id": ObjectId("3e14afdf60b2a486ff731bcc"),
            "tweet_id": ObjectId("aec57084bf77f3c3674c1314"),
            "retweet_id": ObjectId("d670374031f594b09aa7a41d")
        },
        {
            "_id": ObjectId("8fc1574dfb58c6cb2f36c74b"),
            "tweet_id": ObjectId("cc434c34dcb1a0153d2aa318"),
            "retweet_id": ObjectId("1c008d0d7268c7a92fc30a82")
        },
        {
            "_id": ObjectId("0548652a1d54706dd4fdf55c"),
            "tweet_id": ObjectId("fa78002ff2e0db6c41d0dd98"),
            "retweet_id": ObjectId("b8242f58d8b210dc4b042e23")
        },
        {
            "_id": ObjectId("00228e690da0202a00f5d58c"),
            "tweet_id": ObjectId("6bdc747a69faaded84eaaac5"),
            "retweet_id": ObjectId("cf16c5458861d6e6aac06128")
        },
        {
            "_id": ObjectId("f58372d9f95ee3461c075040"),
            "tweet_id": ObjectId("d27c7dbffc8baeb9dfd570d0"),
            "retweet_id": ObjectId("f97a315451ef5dd8ba568050")
        },
        {
            "_id": ObjectId("9e024e75bcb2e03c2dc7dc4b"),
            "tweet_id": ObjectId("5420417fd93a30784e8f2377"),
            "retweet_id": ObjectId("eef7ad93e39646bd2ad12cae")
        },
        {
            "_id": ObjectId("1fecb69db928f27d5f8a16db"),
            "tweet_id": ObjectId("1ce22613f63f853d8ec570a5"),
            "retweet_id": ObjectId("9e7ac68d7c96036e24fa9657")
        },
        {
            "_id": ObjectId("22769485afb21c90fd14bff2"),
            "tweet_id": ObjectId("e6b22822a5f57345255b7af2"),
            "retweet_id": ObjectId("d0350675694c42bd6e7aa5ce")
        },
        {
            "_id": ObjectId("39fe5b6c81db0157de5b10e7"),
            "tweet_id": ObjectId("58492fdafdb454eb9869c8bd"),
            "retweet_id": ObjectId("7207e4336f56fe5f5ebbfe9e")
        },
        {
            "_id": ObjectId("e3bf4075947bc5e644c06ae5"),
            "tweet_id": ObjectId("285066d2876d96d989061a25"),
            "retweet_id": ObjectId("383e0779bfb4f0ec19a38d8d")
        },
        {
            "_id": ObjectId("30b613cc8a9ba76aedb8330a"),
            "tweet_id": ObjectId("4063eeee32daa0ea40241a12"),
            "retweet_id": ObjectId("e37d2c00228d64449c525943")
        },
        {
            "_id": ObjectId("37076ed398753d10823144ed"),
            "tweet_id": ObjectId("e4845b2f7af04d860a805097"),
            "retweet_id": ObjectId("caf5b51838ce8d7dab9e0f5c")
        },
        {
            "_id": ObjectId("f49d51ac7dddab36a7a59ede"),
            "tweet_id": ObjectId("6aa962ed6d303c3c74bd99bb"),
            "retweet_id": ObjectId("0b227d8badfedf8fe8f4411e")
        },
        {
            "_id": ObjectId("aceed5bd5b7df4566bbd5693"),
            "tweet_id": ObjectId("8dfb1bbf36cd57ae0cf5e7c9"),
            "retweet_id": ObjectId("6890257648f4b7c5f83b64c6")
        },
        {
            "_id": ObjectId("12fa39aa973c02983e0843c3"),
            "tweet_id": ObjectId("f59339d6ff3364cc3f46e7f8"),
            "retweet_id": ObjectId("cfdb88fdaf025c97bf9dbd70")
        },
        {
            "_id": ObjectId("b02f6b43aa3bfa1d2d47f7e2"),
            "tweet_id": ObjectId("2d8a31eb39426713ac6f8e8d"),
            "retweet_id": ObjectId("3782fa7adc57b818a0e65649")
        },
        {
            "_id": ObjectId("e0b45d46dc52dbcebe387c65"),
            "tweet_id": ObjectId("56e6c0f63c0f1bb5335ecc18"),
            "retweet_id": ObjectId("eef7ad93e39646bd2ad12cae")
        },
        {
            "_id": ObjectId("775c2074c679cd7d51018ba8"),
            "tweet_id": ObjectId("c1db6accda975e182a7b7715"),
            "retweet_id": ObjectId("35d59d815a7b329317521ad5")
        },
        {
            "_id": ObjectId("199cb5b68c8e6de9b78755ec"),
            "tweet_id": ObjectId("3e595aecfca39e842c077068"),
            "retweet_id": ObjectId("2350f82509fb9d57c9ad2413")
        },
        {
            "_id": ObjectId("a79bc4cec42d06a26290c671"),
            "tweet_id": ObjectId("8ee9b5444a75673b45f28f17"),
            "retweet_id": ObjectId("e622c66954ffa4a327a307fa")
        },
        {
            "_id": ObjectId("59a1118051f9c37bec4b4548"),
            "tweet_id": ObjectId("bbef24cdcd10b722fd53c541"),
            "retweet_id": ObjectId("8eaadcb506142740346ef0f1")
        },
        {
            "_id": ObjectId("39dd34819140512b7d94933a"),
            "tweet_id": ObjectId("36eb194e2c98fb030477e0d4"),
            "retweet_id": ObjectId("13b7a28d6629937b8e6a71f4")
        },
        {
            "_id": ObjectId("d7107505c95074cebb9f653d"),
            "tweet_id": ObjectId("ed742709e12b1c51c11b3d0d"),
            "retweet_id": ObjectId("f8e90f47564c815b912707aa")
        },
        {
            "_id": ObjectId("35356764c66eeff2798d580a"),
            "tweet_id": ObjectId("4e0225fc2c5f426d95ebc8ff"),
            "retweet_id": ObjectId("a4e3ff19f57e55c396cfe525")
        },
        {
            "_id": ObjectId("5cd7dfa6b7b187cb3bcbfefa"),
            "tweet_id": ObjectId("c3e5461c106c90572b7e7743"),
            "retweet_id": ObjectId("906dfe1e228fd63739dafb5b")
        },
        {
            "_id": ObjectId("8d5199cc70270d8aacaf2f30"),
            "tweet_id": ObjectId("018858cc17deb988a4cc6937"),
            "retweet_id": ObjectId("d535e734fdacc41a6a4113db")
        },
        {
            "_id": ObjectId("253b48b8d692a6dda2016f3c"),
            "tweet_id": ObjectId("434349b7071a244d6014c217"),
            "retweet_id": ObjectId("875b8ec1324cb537c44437e2")
        },
        {
            "_id": ObjectId("25340e6ea7341b02810612f8"),
            "tweet_id": ObjectId("be90a095ae2ceda4eb58ee6b"),
            "retweet_id": ObjectId("1b4898cda9336e458d8f4b1f")
        },
        {
            "_id": ObjectId("78308b48db2178b0fa759e6c"),
            "tweet_id": ObjectId("de460234f0359222fbdfc73a"),
            "retweet_id": ObjectId("c56096ab51dc9ba7b61094b9")
        },
        {
            "_id": ObjectId("d41aafd83c3d11a9c94d826b"),
            "tweet_id": ObjectId("bb6568845218edf9d9f862fb"),
            "retweet_id": ObjectId("d185c29b46ad427f3a82c5b8")
        },
        {
            "_id": ObjectId("9e555d39396d115dbed1cac6"),
            "tweet_id": ObjectId("c56096ab51dc9ba7b61094b9"),
            "retweet_id": ObjectId("f2bd9cc99f060b6c8fc80729")
        },
        {
            "_id": ObjectId("12064c83122808e4bd1ba46c"),
            "tweet_id": ObjectId("1427e9f6e380ba51356d074c"),
            "retweet_id": ObjectId("9cb0db3c7ac7ec61161d3ed9")
        },
        {
            "_id": ObjectId("332bb217e14dd8382239d8c3"),
            "tweet_id": ObjectId("e1ec5445d1cecc888d54496d"),
            "retweet_id": ObjectId("4425036d75c651c2a91c80b1")
        },
        {
            "_id": ObjectId("91a94b265784c271a4439f02"),
            "tweet_id": ObjectId("c4b2b7a1c75104837b4007f9"),
            "retweet_id": ObjectId("76abd4c200a153babeb443ac")
        },
        {
            "_id": ObjectId("0217d34937b130f197d294f2"),
            "tweet_id": ObjectId("deb01cc22038303ec1e47024"),
            "retweet_id": ObjectId("f7be074f362c16bd250cdb07")
        },
        {
            "_id": ObjectId("b861fe2fb8777cfeb6b61acf"),
            "tweet_id": ObjectId("048d81c43951b9bbc43814b4"),
            "retweet_id": ObjectId("344d2fbfa5332b1abcd9afbd")
        },
        {
            "_id": ObjectId("f5e63107a8423dc76d0ae908"),
            "tweet_id": ObjectId("fe7eb942ed355955f5716740"),
            "retweet_id": ObjectId("290e5797c1b3db07c73d2bcf")
        },
        {
            "_id": ObjectId("37eaa841f976775d61b04d24"),
            "tweet_id": ObjectId("46729880e3e02fe626349cb6"),
            "retweet_id": ObjectId("914cd55860b3b017a1296795")
        },
        {
            "_id": ObjectId("e556b1aafa7d970a26624276"),
            "tweet_id": ObjectId("bbcc58d10c21d6f9e67dfcb2"),
            "retweet_id": ObjectId("ea53e45dd1c91b5e1c6dceb1")
        },
        {
            "_id": ObjectId("7729f41f37b65e47f23a894d"),
            "tweet_id": ObjectId("04e6d86964e90d31a6ab0258"),
            "retweet_id": ObjectId("fcd2ca1f7c52418a69babce6")
        },
        {
            "_id": ObjectId("f9673068232f996dcb100339"),
            "tweet_id": ObjectId("bebd63cace4aa923fde604a5"),
            "retweet_id": ObjectId("f7324843f743253ceec11adf")
        },
        {
            "_id": ObjectId("9c3c7f27fd5dbe165e960a27"),
            "tweet_id": ObjectId("f93fcc8e5ae5efd14866f271"),
            "retweet_id": ObjectId("08e34ae483947b036cc556a1")
        },
        {
            "_id": ObjectId("6b6827b636747e97c23c6724"),
            "tweet_id": ObjectId("16def66f1f7762050eb44c26"),
            "retweet_id": ObjectId("4d6bca6789d6f680324ca3ca")
        },
        {
            "_id": ObjectId("6724a3cb079963fac5a59198"),
            "tweet_id": ObjectId("1d7b81379ff81e53ea2fc057"),
            "retweet_id": ObjectId("92b42c254bfacb30c1abb894")
        },
        {
            "_id": ObjectId("4e625b8d0fc1c551f1da7618"),
            "tweet_id": ObjectId("9cd731475b465d7a4f1d7cfe"),
            "retweet_id": ObjectId("97ad81526024a9ac03ca8344")
        },
        {
            "_id": ObjectId("9be7604e601e8a6e614cecbd"),
            "tweet_id": ObjectId("d85f53f8c55ce87a8f290ed5"),
            "retweet_id": ObjectId("366c79225dbe5aece420ba17")
        },
        {
            "_id": ObjectId("5faeae668495915d122bd7e8"),
            "tweet_id": ObjectId("0c58e3c70ec810d0b29a0f27"),
            "retweet_id": ObjectId("51415eef1b137e58a8377eaa")
        },
        {
            "_id": ObjectId("ea6a6829e94b6e91e3dc6336"),
            "tweet_id": ObjectId("a34000064ee7223622c08653"),
            "retweet_id": ObjectId("2d3a6a0ad0c53a18d5f4c65e")
        },
        {
            "_id": ObjectId("1183d646020a3176cb4ef3b3"),
            "tweet_id": ObjectId("5ee05248b3b29be8e3c5dc04"),
            "retweet_id": ObjectId("5113a097982fdcc5ed834feb")
        },
        {
            "_id": ObjectId("1cd4db2b026e1f0c6ef1334a"),
            "tweet_id": ObjectId("7e27bc818d800607d459f198"),
            "retweet_id": ObjectId("34b27b93058b0f6b90bffb6a")
        },
        {
            "_id": ObjectId("fb7698b01b873a7aa2d8b315"),
            "tweet_id": ObjectId("8972b98fdf5d8b382ddeb142"),
            "retweet_id": ObjectId("7bea45c0bc836e88ce5d9027")
        },
        {
            "_id": ObjectId("8450ef5e10c93431fce0593e"),
            "tweet_id": ObjectId("3df6483c3c80a6355a00ea3c"),
            "retweet_id": ObjectId("d72a154c3c5c695662fe41e4")
        },
        {
            "_id": ObjectId("dc26130a47f61c06fcedffac"),
            "tweet_id": ObjectId("0bb77cda52a0a875efc39307"),
            "retweet_id": ObjectId("12b400c5f4ff62debff37b3a")
        },
        {
            "_id": ObjectId("2ef903b27e0f62ab1d9f7b9e"),
            "tweet_id": ObjectId("c7be60f6b18a9755caecbdaf"),
            "retweet_id": ObjectId("2a5f3b352819b1a365e805fd")
        },
        {
            "_id": ObjectId("f5ac9992209c5480ee06431f"),
            "tweet_id": ObjectId("bb25400a8781ab709e66f3ad"),
            "retweet_id": ObjectId("22017081e188074c6817f237")
        },
        {
            "_id": ObjectId("80433d86c39adffc61a2c41d"),
            "tweet_id": ObjectId("285066d2876d96d989061a25"),
            "retweet_id": ObjectId("1d24bba11a36d2526b31350f")
        },
        {
            "_id": ObjectId("dd33bf424bda6124435a68c1"),
            "tweet_id": ObjectId("076f602cfec64955501056a8"),
            "retweet_id": ObjectId("88a0604c6e0d9e2c0a061bd8")
        },
        {
            "_id": ObjectId("2f9b955c9e62f7d0cd39297a"),
            "tweet_id": ObjectId("83152e0e9b0377cafd11446c"),
            "retweet_id": ObjectId("1e83411a7f71d435fb478fcc")
        },
        {
            "_id": ObjectId("aeb93d1fc518c8182c696a01"),
            "tweet_id": ObjectId("7c52ca44f4772231799deb7c"),
            "retweet_id": ObjectId("3b217a81fdc05dfffc55fa96")
        },
        {
            "_id": ObjectId("2b700c7d0b52c15fcb358532"),
            "tweet_id": ObjectId("1ea8cf869b450388770acc13"),
            "retweet_id": ObjectId("8b41278f00ab768dd30df7e3")
        },
        {
            "_id": ObjectId("5c51070ede09f8f5feea36c4"),
            "tweet_id": ObjectId("04e769a247ef78d17a030d59"),
            "retweet_id": ObjectId("a4ccec88a373983f3ef83e94")
        },
        {
            "_id": ObjectId("54ca98e714eea2afc127e66a"),
            "tweet_id": ObjectId("73cdf63a696dbb2d4265ba42"),
            "retweet_id": ObjectId("6ef01ba9e23130afbe4c9659")
        },
        {
            "_id": ObjectId("945e18c813887b8a658b6053"),
            "tweet_id": ObjectId("20f5ae05e4e2cb7984391a93"),
            "retweet_id": ObjectId("a9ad7d0360b203161f858291")
        },
        {
            "_id": ObjectId("0a86132080eede3f593c4681"),
            "tweet_id": ObjectId("20dd0f7f2e05b7d851aede70"),
            "retweet_id": ObjectId("d2e109d83a230bc97e73a4f3")
        },
        {
            "_id": ObjectId("384ad9ae95f4706292bf4335"),
            "tweet_id": ObjectId("16c63b40192662ff1346c6c8"),
            "retweet_id": ObjectId("7eefaa3d48aad8ca21f8b96b")
        },
        {
            "_id": ObjectId("a60de019fe2c52223b3285a3"),
            "tweet_id": ObjectId("781cf8a90f49e6dc636aaca9"),
            "retweet_id": ObjectId("d6dca8036753bd8f30c46e10")
        },
        {
            "_id": ObjectId("8fcbe29fe295fb3ad1cfba47"),
            "tweet_id": ObjectId("744f25a7587d14e9e905bc5e"),
            "retweet_id": ObjectId("91d082805397f9fb2c9ab55a")
        },
        {
            "_id": ObjectId("4ed68c34f0f29cb40fcbc0cf"),
            "tweet_id": ObjectId("258828dc1ad307624282c7ac"),
            "retweet_id": ObjectId("517241743fcbfe7ac6147ab0")
        },
        {
            "_id": ObjectId("771f1b71bc863f95b34653aa"),
            "tweet_id": ObjectId("965d5d4fe1105c4f618c8d14"),
            "retweet_id": ObjectId("279ec0c710d5969d059c247c")
        },
        {
            "_id": ObjectId("0185b5e770567c3ab634ac6b"),
            "tweet_id": ObjectId("9fac5d66027917943aab669e"),
            "retweet_id": ObjectId("61796d08397956c37aa5a393")
        },
        {
            "_id": ObjectId("b9d7a8af1aade4c796f99b1f"),
            "tweet_id": ObjectId("766fb6c58ba06e0455fb3ce1"),
            "retweet_id": ObjectId("da961164110d62bc33895293")
        },
        {
            "_id": ObjectId("0d48e65d84e3eefeb7f7d0bd"),
            "tweet_id": ObjectId("1daa049504791826aaa97e58"),
            "retweet_id": ObjectId("94fd149491915e53e1778066")
        },
        {
            "_id": ObjectId("779bf26e4ec5dce88b38efdc"),
            "tweet_id": ObjectId("63e7e7c4a21d93a1bd5e497a"),
            "retweet_id": ObjectId("bc9b7ebabf66163f05704c2f")
        },
        {
            "_id": ObjectId("caa1b0bf3d67540570bc838f"),
            "tweet_id": ObjectId("1bc37814d285ae68cc7b303a"),
            "retweet_id": ObjectId("10b38c1250c48af4c68b3537")
        },
        {
            "_id": ObjectId("089351b038bd0c264c44e19c"),
            "tweet_id": ObjectId("2c3a2e2787c6a78ff75b7341"),
            "retweet_id": ObjectId("a5823b31b25839fb50cde877")
        },
        {
            "_id": ObjectId("e7193b3714bd8dfe06e14a27"),
            "tweet_id": ObjectId("a11e31aaadec3071e5ed323d"),
            "retweet_id": ObjectId("37c295c5a5eadcfefe8f27a4")
        },
        {
            "_id": ObjectId("2e5ff06ad827d2cbc18b453e"),
            "tweet_id": ObjectId("0f7e8cd79b58b90ac1c41b03"),
            "retweet_id": ObjectId("80c89b9d3b19daad3d5a04fa")
        },
        {
            "_id": ObjectId("7d73b55fc9e0baf34b0a3861"),
            "tweet_id": ObjectId("c2394dd8c9d6e2046978d3db"),
            "retweet_id": ObjectId("9679f34da8a9ec45440017a7")
        },
        {
            "_id": ObjectId("c1e7eeaadd7d370de2402532"),
            "tweet_id": ObjectId("1e53016c9a0683dc68582504"),
            "retweet_id": ObjectId("6c227f1fcfc654d6024bd8b6")
        },
        {
            "_id": ObjectId("1f2264475744603d7d0e877c"),
            "tweet_id": ObjectId("4d044145c6b2ec7e36435fbd"),
            "retweet_id": ObjectId("2850ba9c3493d6d7d784951e")
        },
        {
            "_id": ObjectId("c3f570eca8b6517e3a648145"),
            "tweet_id": ObjectId("f9d81ee3a2680287256553ec"),
            "retweet_id": ObjectId("46ef3b41322744d6ad875313")
        },
        {
            "_id": ObjectId("6fb4d555cec2a92e7d71e718"),
            "tweet_id": ObjectId("f1e1084c0665e8194e853195"),
            "retweet_id": ObjectId("4bbc3a26eac7d243b5cd1c6c")
        },
        {
            "_id": ObjectId("bf62bbb8ddf43c53640c1509"),
            "tweet_id": ObjectId("8273d75109a64f913eb5f1e9"),
            "retweet_id": ObjectId("3f0b44df1cfe548da900f208")
        },
        {
            "_id": ObjectId("e71d659e74dd4c5be3cb4df4"),
            "tweet_id": ObjectId("4fe4d72e4a6982106d046d0a"),
            "retweet_id": ObjectId("ed1c16af3bdccbf25a1c4994")
        },
        {
            "_id": ObjectId("1b0955ce6b8c8efff1185376"),
            "tweet_id": ObjectId("729c563bc08626259c973ec2"),
            "retweet_id": ObjectId("f59a9b7524457bc76d469f71")
        },
        {
            "_id": ObjectId("b74f0c1d4a24a242e404df67"),
            "tweet_id": ObjectId("d372a243b7f220237494e1ad"),
            "retweet_id": ObjectId("faae9b225569efae091867e8")
        },
        {
            "_id": ObjectId("5e4028b26df25aedfe3d139d"),
            "tweet_id": ObjectId("432e96c9fc21d133b2769e3f"),
            "retweet_id": ObjectId("d24e7117f088e3f57b421d5e")
        },
        {
            "_id": ObjectId("a04e847c66b96b46d63b541a"),
            "tweet_id": ObjectId("94df469795df666cb8425d44"),
            "retweet_id": ObjectId("7e007a4544f4670d36acb713")
        },
        {
            "_id": ObjectId("7c00e3b55c9cffe848a0c149"),
            "tweet_id": ObjectId("e4aa60a2b75ff689db32155d"),
            "retweet_id": ObjectId("3cb0e62871a780f9261efcce")
        },
        {
            "_id": ObjectId("3b287e0c41a0c25df85c53dc"),
            "tweet_id": ObjectId("f774bbb5bd9a4c7566540b20"),
            "retweet_id": ObjectId("438b6c233b43bfed87bb2a30")
        },
        {
            "_id": ObjectId("fd0696fc92df3de7fe793c6d"),
            "tweet_id": ObjectId("1684c4646c111f6835f9b3ab"),
            "retweet_id": ObjectId("2c0ce2afaadd4ef1a08f8734")
        },
        {
            "_id": ObjectId("c814ac3f54cdcc748e1b0ec6"),
            "tweet_id": ObjectId("52bb0755a2119d9372b2095f"),
            "retweet_id": ObjectId("2427dfdce7b990a6a13e9d25")
        },
        {
            "_id": ObjectId("4fb536934edd302d8d6a04fe"),
            "tweet_id": ObjectId("21d475ff66f3063239a46da2"),
            "retweet_id": ObjectId("34d9a8d8d75422f14d75f5d1")
        },
        {
            "_id": ObjectId("773aeba7101193888ef50935"),
            "tweet_id": ObjectId("cfb8f57c2b3502a84c99350e"),
            "retweet_id": ObjectId("400f602c68ab1da187b47e80")
        },
        {
            "_id": ObjectId("b1f37757288d6a399706a861"),
            "tweet_id": ObjectId("2f869dfab0e81380e00e09b4"),
            "retweet_id": ObjectId("bb69dd0b8fef18d7f7ce9509")
        },
        {
            "_id": ObjectId("55ba7de7721f7c5274b4f300"),
            "tweet_id": ObjectId("6eb52a11ca6c5ba4e0e3d1ef"),
            "retweet_id": ObjectId("9de2e9ddab6b2ff80fb66912")
        },
        {
            "_id": ObjectId("9865ccbcd237532f37ca79ce"),
            "tweet_id": ObjectId("72dc334fa5e5b2b204b943d4"),
            "retweet_id": ObjectId("22c74b920072eaf1a98730a4")
        },
        {
            "_id": ObjectId("cb24470fee4e78a11e856d4e"),
            "tweet_id": ObjectId("13268662c28623e5ff2cacb0"),
            "retweet_id": ObjectId("3caa11789f1383a0a952a770")
        },
        {
            "_id": ObjectId("d0b3fb603c1779552c942d65"),
            "tweet_id": ObjectId("6d7ba1409cf44c6669c1c409"),
            "retweet_id": ObjectId("b0119edfa5bdd12da8fe105e")
        },
        {
            "_id": ObjectId("4237a8aa4db381fddc052376"),
            "tweet_id": ObjectId("6579247acaacb514eff11d43"),
            "retweet_id": ObjectId("1624d7fa7a7890148d88120a")
        },
        {
            "_id": ObjectId("b64ff981d7ee231fada9934d"),
            "tweet_id": ObjectId("5d4e4847fd518e121b178053"),
            "retweet_id": ObjectId("2603eb037e6e3d5e73ced682")
        },
        {
            "_id": ObjectId("bb2e1a5759a12fdc31f829a9"),
            "tweet_id": ObjectId("85968c7a027ccbcd365fd848"),
            "retweet_id": ObjectId("75682596e1a4c1f39e485b66")
        },
        {
            "_id": ObjectId("4c4c7d83d7c3be56c9d5ada7"),
            "tweet_id": ObjectId("def346eed6786953f704d67f"),
            "retweet_id": ObjectId("4169053bc4d89493f033e8df")
        },
        {
            "_id": ObjectId("809cf78a95998ef24456e028"),
            "tweet_id": ObjectId("5ee70e31dddaaa36f1834453"),
            "retweet_id": ObjectId("9e11801dbc4bef596473cc9c")
        },
        {
            "_id": ObjectId("00d9af32903af8aa13e4e783"),
            "tweet_id": ObjectId("5c5e98f863a63f26f2be00de"),
            "retweet_id": ObjectId("4db7ec17067c2fdd427a9bc7")
        },
        {
            "_id": ObjectId("c9cc47bef517fd4a808d5dee"),
            "tweet_id": ObjectId("368ab9fd6415c12aed4e6bc9"),
            "retweet_id": ObjectId("e7515571a59076633577f2ef")
        },
        {
            "_id": ObjectId("64ae902c6a2045aad24014c3"),
            "tweet_id": ObjectId("a4e64c8b853884696350221e"),
            "retweet_id": ObjectId("0a903954524828a4c115a86a")
        },
        {
            "_id": ObjectId("9ef32d0e7bc8f77614db4610"),
            "tweet_id": ObjectId("6807e4f96cc6eb9a1fd748d5"),
            "retweet_id": ObjectId("e096fe9e6c32ac8d0e3804ba")
        },
        {
            "_id": ObjectId("2043488d8b272a7e129bf027"),
            "tweet_id": ObjectId("f272ed53dbf4a837e18046cf"),
            "retweet_id": ObjectId("1f7d1b6a332de838c5c6c388")
        },
        {
            "_id": ObjectId("e9e505746064c8e8556bf82b"),
            "tweet_id": ObjectId("17376b06fd2e0bf778dec4ad"),
            "retweet_id": ObjectId("0581be9274a681af9c09dec4")
        },
        {
            "_id": ObjectId("06236a7808da620c6e971acb"),
            "tweet_id": ObjectId("52b2942df924c897c21e9529"),
            "retweet_id": ObjectId("271a79566e9db6c07d552a20")
        },
        {
            "_id": ObjectId("76433b560883717414004dbc"),
            "tweet_id": ObjectId("2ba236916481c054f71aab9d"),
            "retweet_id": ObjectId("3b285741718196346cd41113")
        },
        {
            "_id": ObjectId("24372897cbb8aa10e2a53374"),
            "tweet_id": ObjectId("7ac0a936b95d154a67e5ac5a"),
            "retweet_id": ObjectId("c59742d10a84f4ef6e2f93c6")
        },
        {
            "_id": ObjectId("3eae7be9844b7163a4218d3f"),
            "tweet_id": ObjectId("fc047c7531d66d9499e398a7"),
            "retweet_id": ObjectId("eef16e12de0e2bb162aba842")
        },
        {
            "_id": ObjectId("4324e21234f56fb36b438619"),
            "tweet_id": ObjectId("b6ff0f2d3ee054e25fe2672f"),
            "retweet_id": ObjectId("f7324843f743253ceec11adf")
        },
        {
            "_id": ObjectId("bc69675a4e03b439f2638b10"),
            "tweet_id": ObjectId("e590d7f48615b83461233676"),
            "retweet_id": ObjectId("eebca6a4d25615418b518477")
        },
        {
            "_id": ObjectId("0b592128cdb397d860289ad7"),
            "tweet_id": ObjectId("b523d9b14cdbe04a7c21fc82"),
            "retweet_id": ObjectId("e4188134e128846da3a5cd55")
        },
        {
            "_id": ObjectId("79e3519e398bf8017d289fb3"),
            "tweet_id": ObjectId("2d654fe20a88b07431129ca8"),
            "retweet_id": ObjectId("b0c70fac24e088d0e9fd3096")
        },
        {
            "_id": ObjectId("cebe990fb2748d9fb8166994"),
            "tweet_id": ObjectId("a81b15b2d50d36c80853ad3b"),
            "retweet_id": ObjectId("73932d4cf80cffd907dfb167")
        },
        {
            "_id": ObjectId("81eff138fe5f0695515e7430"),
            "tweet_id": ObjectId("8e26a3de9bd86d7177b1b5ac"),
            "retweet_id": ObjectId("3e50ed4d795bc9e5dcde3b5d")
        },
        {
            "_id": ObjectId("eed088209d1d342f660c06ac"),
            "tweet_id": ObjectId("79d0c638bc0b6a11391adcb1"),
            "retweet_id": ObjectId("d05c690eb2079caaa60298f7")
        },
        {
            "_id": ObjectId("08f7a8a5bd05f3c6c9badd49"),
            "tweet_id": ObjectId("a9f8b38c7387f6b9f8a12463"),
            "retweet_id": ObjectId("f13e3de8113f49692974f746")
        },
        {
            "_id": ObjectId("cbdeb49cd65f7335e6facc6f"),
            "tweet_id": ObjectId("6492a022ceefa8556714d0aa"),
            "retweet_id": ObjectId("5420417fd93a30784e8f2377")
        },
        {
            "_id": ObjectId("96647bafd539a433ef9210df"),
            "tweet_id": ObjectId("c20f1d249092e6e03009610c"),
            "retweet_id": ObjectId("805543c0a9507d0c3bdd01f1")
        },
        {
            "_id": ObjectId("c65d977a4468273b8c05f9b5"),
            "tweet_id": ObjectId("facb144813abf723dddeabf7"),
            "retweet_id": ObjectId("33a835bdd012912aaf6518be")
        },
        {
            "_id": ObjectId("388a648f5271a85acfe84695"),
            "tweet_id": ObjectId("a387863569a4778b59ce8804"),
            "retweet_id": ObjectId("eafee24678596c4cde903c15")
        },
        {
            "_id": ObjectId("b7f84f6311aa15570f765fb6"),
            "tweet_id": ObjectId("9bb1764823d69958fe3991db"),
            "retweet_id": ObjectId("410fc68fe199658077d03269")
        },
        {
            "_id": ObjectId("a12d7a13e8b86210474ec936"),
            "tweet_id": ObjectId("fe211de3f4273ea639ef097c"),
            "retweet_id": ObjectId("ded66dc73ac6ba5d0c5c3e95")
        },
        {
            "_id": ObjectId("b5b4af77a294a54df48853dc"),
            "tweet_id": ObjectId("44990b1faf260e120c185661"),
            "retweet_id": ObjectId("7085ffbde5cc8b2c04ce17b0")
        },
        {
            "_id": ObjectId("f66873d6895caf4a17cd0d72"),
            "tweet_id": ObjectId("c2b7cc9afeb8811e1946a3bf"),
            "retweet_id": ObjectId("7174239d59533af0f1755c13")
        },
        {
            "_id": ObjectId("a25f1356e32f4dbd87e2b822"),
            "tweet_id": ObjectId("dfdee46dcbd4a961e28485ec"),
            "retweet_id": ObjectId("b3f709ae04deed51590afe40")
        },
        {
            "_id": ObjectId("96c5ce10e1232b7b4617d559"),
            "tweet_id": ObjectId("b62364dd0ef06cd95d73b632"),
            "retweet_id": ObjectId("066927dd4980156a90fa3e32")
        },
        {
            "_id": ObjectId("c3d56b73f46e7ecc4fe78d58"),
            "tweet_id": ObjectId("9f2bb47d967769fb393920a7"),
            "retweet_id": ObjectId("f91fba1d28ff4aaa90f9090f")
        },
        {
            "_id": ObjectId("a33f12fccd71d030e4a029eb"),
            "tweet_id": ObjectId("cb361fff7f764c090e26f7cb"),
            "retweet_id": ObjectId("347edaf39acfefc550b4fc6d")
        },
        {
            "_id": ObjectId("c339e52361647e043580b795"),
            "tweet_id": ObjectId("c893bf9e276bdd0550a7b784"),
            "retweet_id": ObjectId("54807c65bcd5950b2487b06e")
        },
        {
            "_id": ObjectId("a7039e3f255cf8837e69c139"),
            "tweet_id": ObjectId("9900d67121aaf7b92a2d4987"),
            "retweet_id": ObjectId("1b0947b9c65978a22d30d2af")
        },
        {
            "_id": ObjectId("82d7e73fb2057670ef2f4614"),
            "tweet_id": ObjectId("e2543f1af934ebee49acdad1"),
            "retweet_id": ObjectId("4dd113174930f5ff88328c3e")
        },
        {
            "_id": ObjectId("873d8bc6fa250d7051be86a8"),
            "tweet_id": ObjectId("be86b95b132a45fb8354d4cd"),
            "retweet_id": ObjectId("b3656da461e7d17e2444dd1c")
        },
        {
            "_id": ObjectId("5f3e551064bdbbabed349859"),
            "tweet_id": ObjectId("e3393cfe01ef98bc1cea1ea2"),
            "retweet_id": ObjectId("3e7cce149fdbbad0f244d50a")
        },
        {
            "_id": ObjectId("b4c5ba8eb238b1d52bb507ed"),
            "tweet_id": ObjectId("c9d0beff78b9bf571fa562bb"),
            "retweet_id": ObjectId("9444b02b23a479acff964e0d")
        },
        {
            "_id": ObjectId("114db7a5193a865692c7ab0b"),
            "tweet_id": ObjectId("efe9c53c464e420266675e9a"),
            "retweet_id": ObjectId("e38bd1f398ac10c791528ec0")
        },
        {
            "_id": ObjectId("f3da1891994e80eb1e12260c"),
            "tweet_id": ObjectId("6af61746123368029047a533"),
            "retweet_id": ObjectId("07d9c7f099e1fde59c3df84a")
        },
        {
            "_id": ObjectId("f2312bad2098f12e374c994e"),
            "tweet_id": ObjectId("779592060ae73b60a5384d42"),
            "retweet_id": ObjectId("21030977ca6486591e7a5445")
        },
        {
            "_id": ObjectId("297de39c48abb0a6ed2982aa"),
            "tweet_id": ObjectId("25cf7b6c4e801cfb70585482"),
            "retweet_id": ObjectId("fddff9a885f121405fd573c1")
        },
        {
            "_id": ObjectId("52024514cc5bc884488005fc"),
            "tweet_id": ObjectId("d53ee3630f3dd3db0680c268"),
            "retweet_id": ObjectId("4df0ec7f17468b6272079a7e")
        },
        {
            "_id": ObjectId("8b4d2ba06316b24578fd7889"),
            "tweet_id": ObjectId("1fa3f0b1705f68419049a9ff"),
            "retweet_id": ObjectId("b81db2e4a6dbc0822751f82b")
        },
        {
            "_id": ObjectId("48a212704f99b43f43559180"),
            "tweet_id": ObjectId("0b07b11c4c87c202bf7860d3"),
            "retweet_id": ObjectId("285066d2876d96d989061a25")
        },
        {
            "_id": ObjectId("a7747654b32c6a7d3da69e1f"),
            "tweet_id": ObjectId("f8a0481b8b091750057e258a"),
            "retweet_id": ObjectId("d1a027357ae6ff02d577d0cc")
        },
        {
            "_id": ObjectId("f95fb191bbaee365bd067f2d"),
            "tweet_id": ObjectId("842b748494aeca1ff4fab520"),
            "retweet_id": ObjectId("050c34ee9e3159136ea1ee77")
        },
        {
            "_id": ObjectId("8cad5cfb9c2cb58c86eac481"),
            "tweet_id": ObjectId("fad62b5bcef5e2e74dbd7dd2"),
            "retweet_id": ObjectId("8914c295c80c60510c5e5b06")
        },
        {
            "_id": ObjectId("3936aa284347be223cfafdd1"),
            "tweet_id": ObjectId("270a41be401f52eb3e1cafb5"),
            "retweet_id": ObjectId("57a8a4b38d0d8ffb66a9c33b")
        },
        {
            "_id": ObjectId("7b6f6f796b7624b008583289"),
            "tweet_id": ObjectId("6435fccb61186010e2d67744"),
            "retweet_id": ObjectId("b35d13035c8c1957381e9ab5")
        },
        {
            "_id": ObjectId("ec672a474c02a9bbf66962ec"),
            "tweet_id": ObjectId("27b81abbf0cc5a7def19c080"),
            "retweet_id": ObjectId("d01cd2f794b6f6aa850daf8f")
        },
        {
            "_id": ObjectId("ec3f74948520b508aa066449"),
            "tweet_id": ObjectId("5b613fb3a186e73afad893c7"),
            "retweet_id": ObjectId("89acb3dcc19b31784c6a28ad")
        },
        {
            "_id": ObjectId("53b92a580c228600f143b77b"),
            "tweet_id": ObjectId("957211abb4c8ccc43aab3d09"),
            "retweet_id": ObjectId("3c364d14a4b3380b2adb0088")
        },
        {
            "_id": ObjectId("828990dd453aadb6cfd345b8"),
            "tweet_id": ObjectId("05b94e049bf8135a170f340f"),
            "retweet_id": ObjectId("a552690caeaff779aae07b61")
        },
        {
            "_id": ObjectId("45fb6640ef6997dc08744cc2"),
            "tweet_id": ObjectId("5b9070cf1dd571fd18e37278"),
            "retweet_id": ObjectId("f93f0336ccf6746d3e34dca5")
        },
        {
            "_id": ObjectId("1f6bd6287f0e7bb7f22c9077"),
            "tweet_id": ObjectId("29891ced816558f254a5e655"),
            "retweet_id": ObjectId("24d5de31291cbd562afc2834")
        },
        {
            "_id": ObjectId("f1732896e61585f351276a30"),
            "tweet_id": ObjectId("58d6481cddbae5155b9adc1f"),
            "retweet_id": ObjectId("77940cf100aa0b5d0c34ae29")
        },
        {
            "_id": ObjectId("8456b1d7989a64023d0d6bd3"),
            "tweet_id": ObjectId("9996312fd7587aeb7e230a7a"),
            "retweet_id": ObjectId("ab906d1ed0c86f0ede903766")
        },
        {
            "_id": ObjectId("ce5ee2caa735e2b701903993"),
            "tweet_id": ObjectId("dd98525963a3d2c0729c28b9"),
            "retweet_id": ObjectId("b850ee92be110358edb625e2")
        },
        {
            "_id": ObjectId("404e752b5b65341353205e9b"),
            "tweet_id": ObjectId("500ab09054a14d9f069478ee"),
            "retweet_id": ObjectId("521f97101e64c183fb984f5d")
        },
        {
            "_id": ObjectId("23864cd6ebf5b726bf63c6d0"),
            "tweet_id": ObjectId("3b285741718196346cd41113"),
            "retweet_id": ObjectId("553bd03e81f325fb3d03b7da")
        },
        {
            "_id": ObjectId("0bcd6a12fabaf47ca13bf36b"),
            "tweet_id": ObjectId("1b82cfb7b28ea22441406881"),
            "retweet_id": ObjectId("6e57d3c2f203cc772583e2e7")
        },
        {
            "_id": ObjectId("af20054e025062ff9f72b65b"),
            "tweet_id": ObjectId("271a79566e9db6c07d552a20"),
            "retweet_id": ObjectId("30dad2d31373189cc7f0c975")
        },
        {
            "_id": ObjectId("76b21b5213b3a9b9dd5b5667"),
            "tweet_id": ObjectId("2b1e9b74c4e8af0229b3fb97"),
            "retweet_id": ObjectId("71b56701ae9e42225f6ee7b9")
        },
        {
            "_id": ObjectId("ea57c328ababff31e764b7c5"),
            "tweet_id": ObjectId("c0f2df618f0e5cb77c06ae5a"),
            "retweet_id": ObjectId("1eddae145c1584a73d655fc1")
        },
        {
            "_id": ObjectId("26021a2ea129fd191cfa823a"),
            "tweet_id": ObjectId("330e5bef1afa29e8fae60585"),
            "retweet_id": ObjectId("691599e2b726ce0ab3a810c6")
        },
        {
            "_id": ObjectId("46361375be91a38ee794928b"),
            "tweet_id": ObjectId("919510528cf626dbc141c05f"),
            "retweet_id": ObjectId("de460234f0359222fbdfc73a")
        },
        {
            "_id": ObjectId("9500f3d61c50ed1f6e2f9133"),
            "tweet_id": ObjectId("2a7f94d3234143c8266e568b"),
            "retweet_id": ObjectId("4c8d49f923c53a65ef18adbe")
        },
        {
            "_id": ObjectId("a29dd4b021b32146a64bfe66"),
            "tweet_id": ObjectId("31976a270315bf76bedd326f"),
            "retweet_id": ObjectId("0e06d4dff24048f17c193107")
        },
        {
            "_id": ObjectId("4a711b40c9c2b628b106aed8"),
            "tweet_id": ObjectId("54b49582676ff0b512c730a2"),
            "retweet_id": ObjectId("d15f132908975a54016ba821")
        },
        {
            "_id": ObjectId("8bdefb416409e6cf0cadbd97"),
            "tweet_id": ObjectId("3c6d2c4f123827b98713c410"),
            "retweet_id": ObjectId("c455ba278ff2307d2accedb0")
        },
        {
            "_id": ObjectId("d5a72c54913bda8d74db3a19"),
            "tweet_id": ObjectId("c6533ea2ffa436cd39cbe051"),
            "retweet_id": ObjectId("87c228ac85aa5b00bebf748e")
        },
        {
            "_id": ObjectId("36c02cfc29d2d88262534530"),
            "tweet_id": ObjectId("9160063a5c9a5fdacfa17665"),
            "retweet_id": ObjectId("f441cf1abc2cea2d8b1c769d")
        },
        {
            "_id": ObjectId("226d0c635c0f1ffbce41ca0f"),
            "tweet_id": ObjectId("03c18a9eb0077435f1ee171e"),
            "retweet_id": ObjectId("8a4ad84b1f1344da0c1b60ac")
        },
        {
            "_id": ObjectId("e4c400b981128fde7d37ee38"),
            "tweet_id": ObjectId("2bb247e39bece059ef10393c"),
            "retweet_id": ObjectId("f283a69569d4ccee7fefba1c")
        },
        {
            "_id": ObjectId("f18ed2d503fc887443022a4f"),
            "tweet_id": ObjectId("a8d4e6de278dd48e9bf2aeb1"),
            "retweet_id": ObjectId("1185ede99bfb5e66ea4919b0")
        },
        {
            "_id": ObjectId("9f310cfe31adabd80aa16000"),
            "tweet_id": ObjectId("59815403aff2ef06618d3170"),
            "retweet_id": ObjectId("2dbbc46c70e1d2490375f06c")
        },
        {
            "_id": ObjectId("cf94132b6ed21790d0fb7f7c"),
            "tweet_id": ObjectId("7a57e87b088b149aeece67d0"),
            "retweet_id": ObjectId("c37f91b766a75d8c1941f7f2")
        },
        {
            "_id": ObjectId("dbcf0d16544ae108f770b356"),
            "tweet_id": ObjectId("ef4c5e12cc2a51432268da70"),
            "retweet_id": ObjectId("db30c4c7287ebdcda557b7a9")
        },
        {
            "_id": ObjectId("d53abc58304b67bb65bee09e"),
            "tweet_id": ObjectId("eb001378bc5b0c116129598f"),
            "retweet_id": ObjectId("4c23e15e4d1f66bc339c1770")
        },
        {
            "_id": ObjectId("6e573c1cd77af8fe907e4150"),
            "tweet_id": ObjectId("60b9239d0842241944cacd6d"),
            "retweet_id": ObjectId("12a24ed44818a79e5d8453d3")
        },
        {
            "_id": ObjectId("045d2c334b36c5a22cb87333"),
            "tweet_id": ObjectId("ecd3509485f005c62aa22596"),
            "retweet_id": ObjectId("1dafe772590df729ac8ddcfe")
        },
        {
            "_id": ObjectId("23217e2de53df9c98435360c"),
            "tweet_id": ObjectId("a0070722d270644e521d2998"),
            "retweet_id": ObjectId("73e92db8315b67b376fb9fea")
        },
        {
            "_id": ObjectId("06d2d96f6dce5d1cab1903e9"),
            "tweet_id": ObjectId("b23dd176098cdfaa99c289d8"),
            "retweet_id": ObjectId("f42b996d4df7000563ab6a01")
        },
        {
            "_id": ObjectId("a2397d98a0e89aef53be8403"),
            "tweet_id": ObjectId("d421264079640333714812e7"),
            "retweet_id": ObjectId("4eca4500bbb25598f66fe504")
        },
        {
            "_id": ObjectId("3a6f1f99f7bc19b72a76a4d4"),
            "tweet_id": ObjectId("f3bcff12d60a23caeb1d98ff"),
            "retweet_id": ObjectId("711182b24880cd6a25dbd936")
        },
        {
            "_id": ObjectId("691001c199e18eb27bfe5942"),
            "tweet_id": ObjectId("e38bd1f398ac10c791528ec0"),
            "retweet_id": ObjectId("bdb78a7cb75d20a1dca82e68")
        },
        {
            "_id": ObjectId("e5c94b4ada9b377f694ae1cb"),
            "tweet_id": ObjectId("52e82f5dd66907d804316e58"),
            "retweet_id": ObjectId("d7a5d78931a2e798da10da06")
        },
        {
            "_id": ObjectId("bf8853728ceb01b84edf51eb"),
            "tweet_id": ObjectId("302c31a2d54f5052f9bbcd33"),
            "retweet_id": ObjectId("6e2c8379ef20e10d5aa9b572")
        },
        {
            "_id": ObjectId("c26ce9d8c4a01001fde9859e"),
            "tweet_id": ObjectId("388c0cffba55b59fd59fa8d7"),
            "retweet_id": ObjectId("4340454367dc1ab7b303f7ef")
        },
        {
            "_id": ObjectId("6d086d33bbdf73e50a76460d"),
            "tweet_id": ObjectId("bf8903135e0278441c038416"),
            "retweet_id": ObjectId("d51808e6e5d58ec39ff9ae85")
        },
        {
            "_id": ObjectId("9882c94912f9a457b03adf8f"),
            "tweet_id": ObjectId("22f2c00522a9d7858488a098"),
            "retweet_id": ObjectId("4d5f8e8a39b4edf3e70c3a19")
        },
        {
            "_id": ObjectId("c173e1ba35ba9132f02327ad"),
            "tweet_id": ObjectId("45d93d1a86b6851665fcbf9e"),
            "retweet_id": ObjectId("dd222441c4f453c575a74488")
        },
        {
            "_id": ObjectId("568843d185832c1c42714004"),
            "tweet_id": ObjectId("5d6113a3389affe8353207cc"),
            "retweet_id": ObjectId("e60e10e65c1f22c262d61e8a")
        },
        {
            "_id": ObjectId("14cb76a650b8972add79efc9"),
            "tweet_id": ObjectId("d5f85f4b2200b30d8af3ab93"),
            "retweet_id": ObjectId("2b6e4b003c0fa0a3831ef3d3")
        },
        {
            "_id": ObjectId("e569b867b2bfe34b9c0748ad"),
            "tweet_id": ObjectId("4f4af66c12598fa3682d8a3b"),
            "retweet_id": ObjectId("b4106dcd6e5adff236f79cb9")
        },
        {
            "_id": ObjectId("17bb5bf07b83a513a9a7f426"),
            "tweet_id": ObjectId("a99a8a8ff719c1562eccf0c8"),
            "retweet_id": ObjectId("f908eee0abc7e4bab8d27c36")
        },
        {
            "_id": ObjectId("5ec73ebcf6e82a034c124ee9"),
            "tweet_id": ObjectId("55a6f660b37758ef27f33dc4"),
            "retweet_id": ObjectId("050b78f848e32a9764a68e46")
        },
        {
            "_id": ObjectId("8cbf476d0f2fb3ed2b5c7a8a"),
            "tweet_id": ObjectId("ad7f7d8353e52f68504d2468"),
            "retweet_id": ObjectId("4d0bbb7a4c5e6f226e59b145")
        },
        {
            "_id": ObjectId("1f449ff23be0c3bb19553e70"),
            "tweet_id": ObjectId("65e75dbbcbd7c41eebd53416"),
            "retweet_id": ObjectId("aa8ba863587325081dded858")
        },
        {
            "_id": ObjectId("217575e8926fdec755d7db83"),
            "tweet_id": ObjectId("de7a198c12429cbda4e106f2"),
            "retweet_id": ObjectId("0e1ddef1ac3d0b663e4f4587")
        },
        {
            "_id": ObjectId("71f1a46ae28315915b204f1f"),
            "tweet_id": ObjectId("2347dd1c4a18ff4adfe7f253"),
            "retweet_id": ObjectId("95116de5ac0046679258144b")
        },
        {
            "_id": ObjectId("a390665649bc70be70975f6a"),
            "tweet_id": ObjectId("1de7168507853dd100961aea"),
            "retweet_id": ObjectId("17889471af27f78fc6b66fbe")
        },
        {
            "_id": ObjectId("4dbb72e32cde91604aea89eb"),
            "tweet_id": ObjectId("f92becbd863124713b840dbe"),
            "retweet_id": ObjectId("1585164396ab152b18e4337c")
        },
        {
            "_id": ObjectId("22e3248c5ea7ffb6e1af68aa"),
            "tweet_id": ObjectId("1ae52bfb23149b7954e10563"),
            "retweet_id": ObjectId("aeac427c70c74e4c124065e7")
        },
        {
            "_id": ObjectId("22e749c930677cb287947705"),
            "tweet_id": ObjectId("330e5bef1afa29e8fae60585"),
            "retweet_id": ObjectId("ca81b5b73da106483c7786f5")
        },
        {
            "_id": ObjectId("819a8233595cc101c561605b"),
            "tweet_id": ObjectId("0be7b6514c6105084142a2a7"),
            "retweet_id": ObjectId("b8ff72c023ef50c92080cde7")
        },
        {
            "_id": ObjectId("893e66f7398f974e799c50bd"),
            "tweet_id": ObjectId("a208c9747542e58f200bed1a"),
            "retweet_id": ObjectId("e32f1eafee08a290011d758f")
        },
        {
            "_id": ObjectId("04bba7f90f10c614d5c9b6f8"),
            "tweet_id": ObjectId("39ce057b3d89c7d0133fd56a"),
            "retweet_id": ObjectId("3b2594cb4e2e4bfbde2e5f23")
        },
        {
            "_id": ObjectId("92dc9fff97edb731b171f9c7"),
            "tweet_id": ObjectId("74cb434268192fc480f683d6"),
            "retweet_id": ObjectId("a99a8a8ff719c1562eccf0c8")
        },
        {
            "_id": ObjectId("6d25ce8e7f2c16cf6cf76f60"),
            "tweet_id": ObjectId("05d331c834532cab8b0b170d"),
            "retweet_id": ObjectId("aecc530921db19929da1c6f8")
        },
        {
            "_id": ObjectId("d76edf8fe9cf0cca85c1869d"),
            "tweet_id": ObjectId("94df469795df666cb8425d44"),
            "retweet_id": ObjectId("76e30952aa9a70724be35a3b")
        },
        {
            "_id": ObjectId("7497a6c1bbf2910048cbe5bc"),
            "tweet_id": ObjectId("6dd6e00197391368a382c4b1"),
            "retweet_id": ObjectId("badeef6d845295133db8193a")
        },
        {
            "_id": ObjectId("711ba109130265491014fbb1"),
            "tweet_id": ObjectId("b330d2c2be796d7180f056ce"),
            "retweet_id": ObjectId("4eca4500bbb25598f66fe504")
        },
        {
            "_id": ObjectId("f96f79572a9ab7f78e61ada3"),
            "tweet_id": ObjectId("b0b50818f3830cee515170f0"),
            "retweet_id": ObjectId("4c8d49f923c53a65ef18adbe")
        },
        {
            "_id": ObjectId("24e6d35ea58554ea4c9e0076"),
            "tweet_id": ObjectId("ee846f6c58ec9839046bae35"),
            "retweet_id": ObjectId("56294fa3773a472e44e4ef31")
        },
        {
            "_id": ObjectId("14dab72307fcc2320d7eb218"),
            "tweet_id": ObjectId("37c295c5a5eadcfefe8f27a4"),
            "retweet_id": ObjectId("c4d74ce083cf3452eaaccbb5")
        },
        {
            "_id": ObjectId("331981525865a420623a9542"),
            "tweet_id": ObjectId("ef1355690693c64b6ae2ef03"),
            "retweet_id": ObjectId("e8c4f79d1172c404168f02a0")
        },
        {
            "_id": ObjectId("d1a0d0f786950d89db79ea5f"),
            "tweet_id": ObjectId("bc93a2fc2233ba9804ab61ed"),
            "retweet_id": ObjectId("8010d949e8ab447d68a50f55")
        },
        {
            "_id": ObjectId("e01bd0157aaef66a9ab1169e"),
            "tweet_id": ObjectId("fcc591d933ae7907f60b4aa4"),
            "retweet_id": ObjectId("3e7cce149fdbbad0f244d50a")
        },
        {
            "_id": ObjectId("e7026b6cf191647ab4ddf68d"),
            "tweet_id": ObjectId("dd9b557a998769036923b646"),
            "retweet_id": ObjectId("60e18fc07cff63a58486ee92")
        },
        {
            "_id": ObjectId("31e41d8931169df13be9b026"),
            "tweet_id": ObjectId("02323238ce17ee785dd500fa"),
            "retweet_id": ObjectId("027008a17eeee11c4263ed24")
        },
        {
            "_id": ObjectId("8bfcb0615c8d1917c20f36a9"),
            "tweet_id": ObjectId("6b01af7ba199b5f285a54a98"),
            "retweet_id": ObjectId("d50c10495f139665eb046103")
        },
        {
            "_id": ObjectId("1423a509cc1a99663c361600"),
            "tweet_id": ObjectId("afd5a139ebf129cbf06504ed"),
            "retweet_id": ObjectId("92e8e2341deb738d1de8a875")
        },
        {
            "_id": ObjectId("31f995f2c40c56c34f84c201"),
            "tweet_id": ObjectId("95016e73f831d3e1a6d30b52"),
            "retweet_id": ObjectId("c8c75cd669b015a584e5faa3")
        },
        {
            "_id": ObjectId("ffa6f9405c1dbcd654f6c76f"),
            "tweet_id": ObjectId("feedc3deee270e870eab6508"),
            "retweet_id": ObjectId("2e464384f3b1abec43a9d394")
        },
        {
            "_id": ObjectId("d6998822420db306e70df313"),
            "tweet_id": ObjectId("d15f132908975a54016ba821"),
            "retweet_id": ObjectId("810e9664088e2ba9d1fbd076")
        },
        {
            "_id": ObjectId("1e81a1fcb452566d3b286441"),
            "tweet_id": ObjectId("7bae6c87346f14f138720cf4"),
            "retweet_id": ObjectId("68a8a60ae9207f20dfa2c9d1")
        },
        {
            "_id": ObjectId("7a6964c7eeacf6dea0632180"),
            "tweet_id": ObjectId("65d39bdc877b011d4fbd155c"),
            "retweet_id": ObjectId("21bd87237078fb2fb1ad436e")
        },
        {
            "_id": ObjectId("9ea4039a7da0d08d976538f3"),
            "tweet_id": ObjectId("6f516749512da6b58ce5c16f"),
            "retweet_id": ObjectId("72deb2da13fbbfa7ee75cc82")
        },
        {
            "_id": ObjectId("cbb5a464fc62518eca4c9f00"),
            "tweet_id": ObjectId("7ad4a76abc1db9a325932858"),
            "retweet_id": ObjectId("d735bc3ffd7cc24391f07cb3")
        },
        {
            "_id": ObjectId("500c9b1e55ddfb45a98ebf70"),
            "tweet_id": ObjectId("af0ee69018c96c3d49252fe2"),
            "retweet_id": ObjectId("9e4cd93c9614a5295ac4374e")
        },
        {
            "_id": ObjectId("f5610bbb61ca9c0a6407c362"),
            "tweet_id": ObjectId("785431fb280e92bb0a0f60a3"),
            "retweet_id": ObjectId("f58c457f9729cba8e85e198b")
        },
        {
            "_id": ObjectId("df738694c9d6951e606360e4"),
            "tweet_id": ObjectId("5113a097982fdcc5ed834feb"),
            "retweet_id": ObjectId("4b6e8d9fddc38fa2ed57205a")
        },
        {
            "_id": ObjectId("f69c3a83ca640a180b55adf8"),
            "tweet_id": ObjectId("11cf2529108593f80e249133"),
            "retweet_id": ObjectId("cd1403fbe87423c591d1cc29")
        },
        {
            "_id": ObjectId("9690d2ed102cb251340b7b18"),
            "tweet_id": ObjectId("07ef21e4236852b57e669602"),
            "retweet_id": ObjectId("4fe368c1a72c6a9c72c96b80")
        },
        {
            "_id": ObjectId("ad8ed34be71d6704edef3fca"),
            "tweet_id": ObjectId("7ca141c3730133dcc9fbd064"),
            "retweet_id": ObjectId("b3942b6d8eeac184a67e1bcc")
        },
        {
            "_id": ObjectId("4e0e31aff290138c80a2c580"),
            "tweet_id": ObjectId("a54111a91d302571d9da7876"),
            "retweet_id": ObjectId("73e23c5f54448c6ead98958f")
        },
        {
            "_id": ObjectId("19541429b20c4243b60887da"),
            "tweet_id": ObjectId("d75e84744da242532b01c48d"),
            "retweet_id": ObjectId("a7b88941f6fa69e561f7143d")
        },
        {
            "_id": ObjectId("1c0a4d5860b43477980f0f0a"),
            "tweet_id": ObjectId("efd858c3c7a5bcf14968427b"),
            "retweet_id": ObjectId("ecc7467fcb3ce9a1b8baa693")
        },
        {
            "_id": ObjectId("0c67fef7842e1886c653a894"),
            "tweet_id": ObjectId("1caa0274b4b04345fcafa0cd"),
            "retweet_id": ObjectId("34b27b93058b0f6b90bffb6a")
        },
        {
            "_id": ObjectId("4c24b37a330490f6765ed3d9"),
            "tweet_id": ObjectId("eb9d5724e1bef7ba466de494"),
            "retweet_id": ObjectId("7eed78a701953bf49f8e5654")
        },
        {
            "_id": ObjectId("3d389b806d69c61f7c95e276"),
            "tweet_id": ObjectId("cbf426b8f0efcabb5e4174a5"),
            "retweet_id": ObjectId("938450b20f8f096d740dc6e1")
        },
        {
            "_id": ObjectId("160364cb7513898209f9de9a"),
            "tweet_id": ObjectId("cc5c4d1d3e828718a9252542"),
            "retweet_id": ObjectId("18ebb939ba9ff6270d444368")
        },
        {
            "_id": ObjectId("a75219b66c15a7822236d5f8"),
            "tweet_id": ObjectId("1c6b88389ce768f22e435689"),
            "retweet_id": ObjectId("b0b6e401c26394b6b687dcb2")
        },
        {
            "_id": ObjectId("bdb93276113ea667dff00638"),
            "tweet_id": ObjectId("a5c3e791ace5724b8eeacf82"),
            "retweet_id": ObjectId("6f084706c076ed112bb13946")
        },
        {
            "_id": ObjectId("29370549931e3977a6d93841"),
            "tweet_id": ObjectId("406f54750c4aa56c77e02b2c"),
            "retweet_id": ObjectId("fbccdd70b1171eddc62c8740")
        },
        {
            "_id": ObjectId("995112394b3a3a0ebeb28950"),
            "tweet_id": ObjectId("e381a7fce144b1a8007d30ca"),
            "retweet_id": ObjectId("21a0c5299bb4adc2d5df3b9d")
        },
        {
            "_id": ObjectId("39ea3434a68b37b91ca56a3a"),
            "tweet_id": ObjectId("c59c99584b4964a287d4e1c9"),
            "retweet_id": ObjectId("7d4321e426129e3ae74014df")
        },
        {
            "_id": ObjectId("4be5cdd6829a6f7f8f760802"),
            "tweet_id": ObjectId("31f0cbe15d8864309b864faa"),
            "retweet_id": ObjectId("20f785eafab9e74227a3ce0a")
        },
        {
            "_id": ObjectId("8c97fc94355e642946ecb486"),
            "tweet_id": ObjectId("54462aee4857cc6bf97affbf"),
            "retweet_id": ObjectId("659b3c19743472868cc077cd")
        },
        {
            "_id": ObjectId("b8866ae076642807c5bb79d5"),
            "tweet_id": ObjectId("8dfb1bbf36cd57ae0cf5e7c9"),
            "retweet_id": ObjectId("421a0b3c5b15881d6fccab42")
        },
        {
            "_id": ObjectId("36f449090351c3008867eda7"),
            "tweet_id": ObjectId("0f4354e4991d3475f89aef51"),
            "retweet_id": ObjectId("69b322f2902e003036cf2ec8")
        },
        {
            "_id": ObjectId("277407b65dc77298bd6a42f5"),
            "tweet_id": ObjectId("867dcafec9e1be819e81b978"),
            "retweet_id": ObjectId("441a3198711737ce0d4b5a21")
        },
        {
            "_id": ObjectId("b9feb37cf6508f005daa3056"),
            "tweet_id": ObjectId("f58c457f9729cba8e85e198b"),
            "retweet_id": ObjectId("a8cc70385fb2c9d6f25321ae")
        },
        {
            "_id": ObjectId("24005ad7d230d15b1068869e"),
            "tweet_id": ObjectId("9244ddc899efd47bbf5ba420"),
            "retweet_id": ObjectId("b0119edfa5bdd12da8fe105e")
        },
        {
            "_id": ObjectId("a20ee0d094e329fb73fb4689"),
            "tweet_id": ObjectId("6f368db6408ba5392d91886a"),
            "retweet_id": ObjectId("31c4c1e2889f0fc5ad78f0d6")
        },
        {
            "_id": ObjectId("c63df16004650f64149f3951"),
            "tweet_id": ObjectId("45d882195746171cbb3ca9e3"),
            "retweet_id": ObjectId("4b6b664204dcca4e94fdbb1b")
        },
        {
            "_id": ObjectId("01634561d0685000e2504065"),
            "tweet_id": ObjectId("d56a58072cd4e5813327275c"),
            "retweet_id": ObjectId("5d9721331d8617b2b73c1691")
        },
        {
            "_id": ObjectId("42227035f1d2df5b5c033f6b"),
            "tweet_id": ObjectId("5f64e5ea548d33f8d228d26c"),
            "retweet_id": ObjectId("d5ea0d2351f02a9d3572f367")
        },
        {
            "_id": ObjectId("80abb18653cedc29f21d071c"),
            "tweet_id": ObjectId("7eb9c9c3fedeac0be5612db8"),
            "retweet_id": ObjectId("c711f1a2fb8df7a968178c79")
        },
        {
            "_id": ObjectId("96cda823d2f37e00a772dfce"),
            "tweet_id": ObjectId("d1a027357ae6ff02d577d0cc"),
            "retweet_id": ObjectId("b418bdb1a618f1b2908bb668")
        },
        {
            "_id": ObjectId("7c12ac5e9c58983fc47ef87d"),
            "tweet_id": ObjectId("4d9b402c6e4a51a5d5e17e3c"),
            "retweet_id": ObjectId("657ee6cb7444348c02c8c33b")
        },
        {
            "_id": ObjectId("4227ddf0369fdfd657ab3c81"),
            "tweet_id": ObjectId("25bc16285394bb3c23e81367"),
            "retweet_id": ObjectId("d72a154c3c5c695662fe41e4")
        },
        {
            "_id": ObjectId("9f10f681187854155a634e57"),
            "tweet_id": ObjectId("fe34b6bbeefa39278fbb92d5"),
            "retweet_id": ObjectId("0138738faa874b5b9e9c60d2")
        },
        {
            "_id": ObjectId("1bdc041651c126ebe49791d7"),
            "tweet_id": ObjectId("db380f99e9fe1c343b95fb0a"),
            "retweet_id": ObjectId("2fe4d8c0dc73eda397f0bc02")
        },
        {
            "_id": ObjectId("0870e59411960f05536753f3"),
            "tweet_id": ObjectId("3c90285023862f66300ef06f"),
            "retweet_id": ObjectId("21e0e933f98f243c6d356238")
        },
        {
            "_id": ObjectId("f1b4cc7feb33e0ac829d482d"),
            "tweet_id": ObjectId("81d27569224f6bb1235af7eb"),
            "retweet_id": ObjectId("507576899b03b6123347e2b3")
        },
        {
            "_id": ObjectId("99971829c45abcf059c909c8"),
            "tweet_id": ObjectId("b32b35a13edfb713647ab71b"),
            "retweet_id": ObjectId("6b904f1f248d9633fa9a3ebf")
        },
        {
            "_id": ObjectId("f117acadbebb98ad587f8c1e"),
            "tweet_id": ObjectId("9d346abc8b38f1812c161786"),
            "retweet_id": ObjectId("7b998caa32ef46b565b0dcce")
        },
        {
            "_id": ObjectId("23bb1ae37164d7685b837c1b"),
            "tweet_id": ObjectId("920c193d4da34bbf25f1787f"),
            "retweet_id": ObjectId("34b47a42d14e67023c6931d3")
        },
        {
            "_id": ObjectId("4ad021e451870b4952269107"),
            "tweet_id": ObjectId("9da5a94158f292c9f6e09388"),
            "retweet_id": ObjectId("096fe7da067a4a99eac0195b")
        },
        {
            "_id": ObjectId("ae6aa282ccfb3a39783d3d87"),
            "tweet_id": ObjectId("56e6c0f63c0f1bb5335ecc18"),
            "retweet_id": ObjectId("55a6f660b37758ef27f33dc4")
        },
        {
            "_id": ObjectId("f65c058c1afdcaa68f5b4bb2"),
            "tweet_id": ObjectId("6fa7b4d61bce578ef9271439"),
            "retweet_id": ObjectId("4494b6b9007b314a941375aa")
        },
        {
            "_id": ObjectId("129bc790288e95873fcde2b1"),
            "tweet_id": ObjectId("f7be074f362c16bd250cdb07"),
            "retweet_id": ObjectId("4b69e414c17a5e24bcf22ad8")
        },
        {
            "_id": ObjectId("5ec2cd098e55d224f1eff8e4"),
            "tweet_id": ObjectId("deac97b3af74b5237e6c7690"),
            "retweet_id": ObjectId("027008a17eeee11c4263ed24")
        },
        {
            "_id": ObjectId("30cc43cd3e0032b6772c2e6b"),
            "tweet_id": ObjectId("147ba7f31c7f6efc30e09345"),
            "retweet_id": ObjectId("9383d72dc948efe2a1439f1c")
        },
        {
            "_id": ObjectId("f8f6dc6f66614b8d73e29bc9"),
            "tweet_id": ObjectId("13db86c2f7720f42b44fab5d"),
            "retweet_id": ObjectId("4f4af66c12598fa3682d8a3b")
        },
        {
            "_id": ObjectId("151149b1be6b3f74c158e5e4"),
            "tweet_id": ObjectId("d51a5561ccae3f08107f09bf"),
            "retweet_id": ObjectId("f92480f54f497d12cc922a3e")
        },
        {
            "_id": ObjectId("fed28ef50ac942038d5d5fd5"),
            "tweet_id": ObjectId("50db58e4fa0b831998d7ded2"),
            "retweet_id": ObjectId("c22f2ff2e17150c67f9facf0")
        },
        {
            "_id": ObjectId("cc8ab98073e1a3a77669581b"),
            "tweet_id": ObjectId("e6b139b1b230c08c99b474f8"),
            "retweet_id": ObjectId("10b38c1250c48af4c68b3537")
        },
        {
            "_id": ObjectId("bede2549e455be347837da38"),
            "tweet_id": ObjectId("50ef5543d0a1d933840f1b37"),
            "retweet_id": ObjectId("2d8a31eb39426713ac6f8e8d")
        },
        {
            "_id": ObjectId("76b1a11a9620a41f909d9643"),
            "tweet_id": ObjectId("fc607b2259b83468f425c585"),
            "retweet_id": ObjectId("ad182531e39aa0909fceb2fd")
        },
        {
            "_id": ObjectId("72e4371b1be0bd419ef93eef"),
            "tweet_id": ObjectId("c9f0f58e2ff0fd9ec96d89ad"),
            "retweet_id": ObjectId("25b7c27bc0bc664a1dc52fc2")
        },
        {
            "_id": ObjectId("7f2388e77ab262756637e828"),
            "tweet_id": ObjectId("e57c96e6d00a2663c1c95f61"),
            "retweet_id": ObjectId("6741c7f459b3a134e1a11c25")
        },
        {
            "_id": ObjectId("10bf513924fbb54ffc8c6caf"),
            "tweet_id": ObjectId("fea3511c80651595fe291c14"),
            "retweet_id": ObjectId("f9dfe87b27c00bcf8104187a")
        },
        {
            "_id": ObjectId("644383433863ec879f099566"),
            "tweet_id": ObjectId("c24ecd4300054495d8be792b"),
            "retweet_id": ObjectId("fa4cc2c8ef6f2d066314dba3")
        },
        {
            "_id": ObjectId("88eb19325ec2157ac4e7a003"),
            "tweet_id": ObjectId("5d6113a3389affe8353207cc"),
            "retweet_id": ObjectId("aa84e756c3cf43e420096c61")
        },
        {
            "_id": ObjectId("3f5b02ab7d6a5e639c761c8c"),
            "tweet_id": ObjectId("68e3ca5d8eaf6f7c7ab8b6f7"),
            "retweet_id": ObjectId("985f00e9ddf73d5df5999d1d")
        },
        {
            "_id": ObjectId("f63dcc1ee1dac95ede9f6cc7"),
            "tweet_id": ObjectId("65e924bd4c9bf9635fa171af"),
            "retweet_id": ObjectId("441a3198711737ce0d4b5a21")
        },
        {
            "_id": ObjectId("e4d68be0e54feb8bad9c1110"),
            "tweet_id": ObjectId("f8e340a4593cff28a6674b36"),
            "retweet_id": ObjectId("aa8adead9aefb5b14ce3bf79")
        },
        {
            "_id": ObjectId("380f9afec34d39b43570503b"),
            "tweet_id": ObjectId("b17c25b18bb8f0bd745230b7"),
            "retweet_id": ObjectId("f1df9b098c3aeac6a2651b66")
        },
        {
            "_id": ObjectId("1368a55a3bf690d2cc6749ba"),
            "tweet_id": ObjectId("e49688fff3b4043672c68b80"),
            "retweet_id": ObjectId("d535e734fdacc41a6a4113db")
        },
        {
            "_id": ObjectId("fcb0df648f7e2ee5d04b2714"),
            "tweet_id": ObjectId("c260a999f2725c0917711eb0"),
            "retweet_id": ObjectId("c1db6accda975e182a7b7715")
        },
        {
            "_id": ObjectId("cde850e3c2dc0482fc72d4f1"),
            "tweet_id": ObjectId("7a8faac342b02efe4f328d81"),
            "retweet_id": ObjectId("076f602cfec64955501056a8")
        },
        {
            "_id": ObjectId("29b24c48ee992b09d40e20b3"),
            "tweet_id": ObjectId("18900c1465cf87579671d931"),
            "retweet_id": ObjectId("d99b9683378c1bd70a162142")
        },
        {
            "_id": ObjectId("a93e06548bbec2c1724febb2"),
            "tweet_id": ObjectId("9bae362994da7261eb449393"),
            "retweet_id": ObjectId("4ba2ce07e5abb98412261779")
        },
        {
            "_id": ObjectId("9c7c80ffff4137dfd8ee9642"),
            "tweet_id": ObjectId("bbff14d0f2cfb28e9ad417cb"),
            "retweet_id": ObjectId("c58427b7b185a3c3b8545727")
        },
        {
            "_id": ObjectId("200d39e1c3b401d1f0e1037f"),
            "tweet_id": ObjectId("5c28e5690f6b285d35610269"),
            "retweet_id": ObjectId("03f12a81ec66ab456785d921")
        },
        {
            "_id": ObjectId("6033f23d7a53e8e6c967f050"),
            "tweet_id": ObjectId("4824d54b9e56ad95656f65e9"),
            "retweet_id": ObjectId("8af87f94d90903718ea3429e")
        },
        {
            "_id": ObjectId("616d903cbd82bea84d31aa3f"),
            "tweet_id": ObjectId("6b9bf07d3b0e8fa7d197c1a7"),
            "retweet_id": ObjectId("6e89c48988d6dc72a140325d")
        },
        {
            "_id": ObjectId("2835d5afa14436cb25b7e9ab"),
            "tweet_id": ObjectId("fa43d35873d83ad0412c5902"),
            "retweet_id": ObjectId("72bedbe76f730c94bf04b999")
        },
        {
            "_id": ObjectId("b3588dcd3543c7b62dd6d90f"),
            "tweet_id": ObjectId("84e1c89e0b4aca5b5f4ae0ac"),
            "retweet_id": ObjectId("38fad8aaa1540afa00d2d404")
        },
        {
            "_id": ObjectId("7e207e002d5ed5b9c9b4eb61"),
            "tweet_id": ObjectId("419d196415f1f9fb9fac6bff"),
            "retweet_id": ObjectId("b74b089a1f49cc494a24f1ca")
        },
        {
            "_id": ObjectId("66d2cc1592812c727cfe3d76"),
            "tweet_id": ObjectId("edfd38d4d134f3d495142072"),
            "retweet_id": ObjectId("84cf529617fe576b88632503")
        },
        {
            "_id": ObjectId("5362b84a0611190392dc263a"),
            "tweet_id": ObjectId("bd73fe73f5514a331693d2a8"),
            "retweet_id": ObjectId("1e3f8975f7f410a4eafd56ea")
        },
        {
            "_id": ObjectId("d3799f48009c9cef52de8608"),
            "tweet_id": ObjectId("91427b87dbf0d6d5f8c52642"),
            "retweet_id": ObjectId("05276bf4aa96ed3847ee716e")
        },
        {
            "_id": ObjectId("44e3a3e7e4773093e6b1240c"),
            "tweet_id": ObjectId("ef2c912ef5a77feb2a23b981"),
            "retweet_id": ObjectId("b523d9b14cdbe04a7c21fc82")
        },
        {
            "_id": ObjectId("e4718f0d2dd30cf008eda19a"),
            "tweet_id": ObjectId("d967983f390e9c8aaddd254b"),
            "retweet_id": ObjectId("95335ec613f3c21dd6b8a427")
        },
        {
            "_id": ObjectId("df84ae7ab2fc4eb373acd3cc"),
            "tweet_id": ObjectId("21fae6193a31c38a35f19cec"),
            "retweet_id": ObjectId("b463e902c262e845311d346b")
        },
        {
            "_id": ObjectId("cf32afd3f12c3cc3d8722683"),
            "tweet_id": ObjectId("01a12028ca822231ff569919"),
            "retweet_id": ObjectId("37bb9f2a4226b954987d4acc")
        },
        {
            "_id": ObjectId("75f04d47a54d866917a8640b"),
            "tweet_id": ObjectId("1bd4ac89fd04e61a45cfa52f"),
            "retweet_id": ObjectId("25b3ac142ffd22254d0f9742")
        },
        {
            "_id": ObjectId("1caaebd9248e93243dd942cb"),
            "tweet_id": ObjectId("bd251f44aacb4cda690c7f18"),
            "retweet_id": ObjectId("12045298737e63bf2e1a9fda")
        },
        {
            "_id": ObjectId("adf8deb6a98647b5c8983ace"),
            "tweet_id": ObjectId("a296f7f2655670298ccc760e"),
            "retweet_id": ObjectId("3443547b708ead4a48e85c98")
        },
        {
            "_id": ObjectId("5c95147ea4310c36e9894c8b"),
            "tweet_id": ObjectId("8343dcb98b61c31c1baa440a"),
            "retweet_id": ObjectId("e4f5583d20659e7afd39e0dc")
        },
        {
            "_id": ObjectId("3ea9d6971f28c053fd4c092f"),
            "tweet_id": ObjectId("49b9ea9a2e1bab9d6b39894f"),
            "retweet_id": ObjectId("d02ce2c564f2be85566b190c")
        },
        {
            "_id": ObjectId("c3a54fa0636479b48c41b66a"),
            "tweet_id": ObjectId("09e00a265ee26c1a2105a9ca"),
            "retweet_id": ObjectId("875b8ec1324cb537c44437e2")
        },
        {
            "_id": ObjectId("e525eb588f87c26309311e9a"),
            "tweet_id": ObjectId("e811fa70ee5e03f399b8ee71"),
            "retweet_id": ObjectId("708d999e05e22d5ba972f87b")
        },
        {
            "_id": ObjectId("cdf9177edafe016746c1ef68"),
            "tweet_id": ObjectId("9f53a3c20bab47ed371958b6"),
            "retweet_id": ObjectId("ef457e4b5d93dbdb40ca65cb")
        },
        {
            "_id": ObjectId("5a5f881b4bafb686cbd78480"),
            "tweet_id": ObjectId("c59742d10a84f4ef6e2f93c6"),
            "retweet_id": ObjectId("3cb0e62871a780f9261efcce")
        },
        {
            "_id": ObjectId("95d82007de35f5db4903cb78"),
            "tweet_id": ObjectId("92e150bb800b607859198bf6"),
            "retweet_id": ObjectId("2c41e26d14dfab9148542487")
        },
        {
            "_id": ObjectId("0e08c3e40a8460483186f2f3"),
            "tweet_id": ObjectId("178e05035dd7d52b04a03100"),
            "retweet_id": ObjectId("9da370152889bdd3cad45536")
        },
        {
            "_id": ObjectId("1ece7651ca8ac4932301705d"),
            "tweet_id": ObjectId("20dd0f7f2e05b7d851aede70"),
            "retweet_id": ObjectId("673c97b205d30fa39816ace0")
        },
        {
            "_id": ObjectId("0efb93c5505421299f7edcac"),
            "tweet_id": ObjectId("40b3a8c2f0ca5e581b88df8d"),
            "retweet_id": ObjectId("8d35e8c41e5bc8f7d70d50c0")
        },
        {
            "_id": ObjectId("a1ff439236df9882ea9600a9"),
            "tweet_id": ObjectId("b9af69d02be324e3ed8d4541"),
            "retweet_id": ObjectId("47c8427fad15bab1b5f24794")
        },
        {
            "_id": ObjectId("4f59b9c6bcda90021ff7d55d"),
            "tweet_id": ObjectId("e381a7fce144b1a8007d30ca"),
            "retweet_id": ObjectId("c4d74ce083cf3452eaaccbb5")
        },
        {
            "_id": ObjectId("515d8ab15944070ccc3adafb"),
            "tweet_id": ObjectId("1b82cfb7b28ea22441406881"),
            "retweet_id": ObjectId("456156a826cfbf16054b3b72")
        },
        {
            "_id": ObjectId("a34b89f8872effc15ecc729d"),
            "tweet_id": ObjectId("97e18863d46d04d891210900"),
            "retweet_id": ObjectId("62d773fedcb0074a6f9b802f")
        },
        {
            "_id": ObjectId("ef6577ce35c423ee77a12e29"),
            "tweet_id": ObjectId("82e4d986d9d4bbfc947e75de"),
            "retweet_id": ObjectId("63e7e7c4a21d93a1bd5e497a")
        },
        {
            "_id": ObjectId("cc132b6688ba0754c8e21afd"),
            "tweet_id": ObjectId("ddac992c0ef75110ad6b0d52"),
            "retweet_id": ObjectId("eafee24678596c4cde903c15")
        },
        {
            "_id": ObjectId("9d3b600cf6b3ee7244b1d7c1"),
            "tweet_id": ObjectId("ca3da1ed8060a161159b30a6"),
            "retweet_id": ObjectId("930e11d6eab8f3e30eecb8a4")
        },
        {
            "_id": ObjectId("72cd2cd34c07d5a3b8106f83"),
            "tweet_id": ObjectId("1ba1c9c1ca60dc6f376c09de"),
            "retweet_id": ObjectId("384f5e67a3fef09fcb8d3a9d")
        },
        {
            "_id": ObjectId("7a60fe7255664c7f87317eb3"),
            "tweet_id": ObjectId("ab0963d1928b08e41f778994"),
            "retweet_id": ObjectId("bdd9e6e569c0cba9be5c2be1")
        },
        {
            "_id": ObjectId("2cdae4fbf1fb84fa44a8ce34"),
            "tweet_id": ObjectId("40a6ea7b98b1f145353d3f18"),
            "retweet_id": ObjectId("57b9a12850bd6cd1c4b80b66")
        },
        {
            "_id": ObjectId("68c09c5a734d335dc29025d7"),
            "tweet_id": ObjectId("f38b091b98d2e7386047c392"),
            "retweet_id": ObjectId("574ec756d83ac95e3488457a")
        },
        {
            "_id": ObjectId("d17353de2e432deaead02760"),
            "tweet_id": ObjectId("859a460144c3c610479a312e"),
            "retweet_id": ObjectId("343d239c26dfbb7b0df48d66")
        },
        {
            "_id": ObjectId("19790fbe20793800eee4d27f"),
            "tweet_id": ObjectId("1389ba6d493f3e128c17a24b"),
            "retweet_id": ObjectId("362cd8102b80c9746151e66d")
        },
        {
            "_id": ObjectId("88852095111dcb723c73c7e8"),
            "tweet_id": ObjectId("076f602cfec64955501056a8"),
            "retweet_id": ObjectId("da8613cd862bf8a09f921405")
        },
        {
            "_id": ObjectId("2963392ce3723016dff86c13"),
            "tweet_id": ObjectId("fc0c7decf3812c12426d386c"),
            "retweet_id": ObjectId("73e6d6014514f7f1ade557d7")
        },
        {
            "_id": ObjectId("24738bc3a5935a00ef638cb3"),
            "tweet_id": ObjectId("d3560f2463561f441b6bfdc5"),
            "retweet_id": ObjectId("5900aeec9e767f23192d4fbc")
        },
        {
            "_id": ObjectId("85b83201ba6e8ecf9db32405"),
            "tweet_id": ObjectId("dbaf48bf353dce1c9711277f"),
            "retweet_id": ObjectId("d7a17530916bc9285a0cf813")
        },
        {
            "_id": ObjectId("6ce985d7168266d55504e40c"),
            "tweet_id": ObjectId("18e98d71097e0a0d6c046f9a"),
            "retweet_id": ObjectId("bbd4766ec835dc04fea9db7a")
        },
        {
            "_id": ObjectId("7bb11b3f07e881c83ba2718a"),
            "tweet_id": ObjectId("7e007a4544f4670d36acb713"),
            "retweet_id": ObjectId("f00847a23ccac0bc64629739")
        },
        {
            "_id": ObjectId("ee8103a99065a346afebfc8a"),
            "tweet_id": ObjectId("2670dd5e87d82b83ed26c35f"),
            "retweet_id": ObjectId("bc398bca787ec90546a2e8de")
        },
        {
            "_id": ObjectId("97fa1d37a5a81f801a8c01e1"),
            "tweet_id": ObjectId("507cc0c7396f83ec0acdf56b"),
            "retweet_id": ObjectId("ac37f68bd7460ae4572262fe")
        },
        {
            "_id": ObjectId("7005f2afb5bc81489c616be7"),
            "tweet_id": ObjectId("8730ffe7242f541884ba1697"),
            "retweet_id": ObjectId("e486051a5e5a4cd4e66b50f2")
        },
        {
            "_id": ObjectId("8c2824de5ab3dc0ed707cba8"),
            "tweet_id": ObjectId("487e65ad9a0fbffab3380398"),
            "retweet_id": ObjectId("52670d31e9923a675a43c6a2")
        },
        {
            "_id": ObjectId("ca5e70f745eaa62428df784f"),
            "tweet_id": ObjectId("de7a198c12429cbda4e106f2"),
            "retweet_id": ObjectId("c65fd2f18c324348ebcd7e51")
        },
        {
            "_id": ObjectId("989e4df5cce6c1b5397ae254"),
            "tweet_id": ObjectId("a7db90e5f737dd3de7f1d56e"),
            "retweet_id": ObjectId("9f4e221c80f87b02240900d4")
        },
        {
            "_id": ObjectId("254719e6e1b2350d2d2c251e"),
            "tweet_id": ObjectId("281d2b8b6e667049c03bb5aa"),
            "retweet_id": ObjectId("4494b6b9007b314a941375aa")
        },
        {
            "_id": ObjectId("0a60ce6b794e9ce4bbc03458"),
            "tweet_id": ObjectId("8ee9b5444a75673b45f28f17"),
            "retweet_id": ObjectId("37c8d84dbe743e5810dc094d")
        },
        {
            "_id": ObjectId("79819c2ebc1260893fec771d"),
            "tweet_id": ObjectId("1019d52b897a21a7bc13d1a8"),
            "retweet_id": ObjectId("a4e64c8b853884696350221e")
        },
        {
            "_id": ObjectId("a88eb3a8a6fc5847bbf4a36a"),
            "tweet_id": ObjectId("023458706b008511209cd3a0"),
            "retweet_id": ObjectId("53382f3ed7916140288171b5")
        },
        {
            "_id": ObjectId("9692dc9297a52854880f75eb"),
            "tweet_id": ObjectId("ae897c95db0fe1f20540a216"),
            "retweet_id": ObjectId("d4b2c6aa1e68fba41229c9e7")
        },
        {
            "_id": ObjectId("6a48d94863d70bd4ee0a4007"),
            "tweet_id": ObjectId("ccebf459c93c6eea34839255"),
            "retweet_id": ObjectId("4e33e77f20a62ff71aae9ece")
        },
        {
            "_id": ObjectId("085f9798ae906b21628970d4"),
            "tweet_id": ObjectId("5f7762158cee356f96c66a97"),
            "retweet_id": ObjectId("1b4898cda9336e458d8f4b1f")
        },
        {
            "_id": ObjectId("dfdd06b338140172831b17c2"),
            "tweet_id": ObjectId("1a7274acf572e5aaf2466f67"),
            "retweet_id": ObjectId("2876c5d34e36fffe4e2d9a25")
        },
        {
            "_id": ObjectId("9161c085134b76629ec02ccb"),
            "tweet_id": ObjectId("13ed2f56de4a902610d016fa"),
            "retweet_id": ObjectId("e61591a1efc1ef66be9d9e12")
        },
        {
            "_id": ObjectId("5a8535ec92915cf3a2553667"),
            "tweet_id": ObjectId("425a4457ba56832e7f02a393"),
            "retweet_id": ObjectId("fad62b5bcef5e2e74dbd7dd2")
        },
        {
            "_id": ObjectId("605aa08364e6012e00e96232"),
            "tweet_id": ObjectId("0d149238657d3196b7b49853"),
            "retweet_id": ObjectId("5e428f0ec78f2703ea817429")
        },
        {
            "_id": ObjectId("7fdf960c39d046a9d8301ffd"),
            "tweet_id": ObjectId("aecc530921db19929da1c6f8"),
            "retweet_id": ObjectId("63a7d432145d3f4ca641d3d7")
        },
        {
            "_id": ObjectId("b1820c67352dfe810cd57e1c"),
            "tweet_id": ObjectId("bb0c12bd135b7c52c9839b85"),
            "retweet_id": ObjectId("95916b5caa97eb10943e7515")
        },
        {
            "_id": ObjectId("74dcc640dfe6234b95fca853"),
            "tweet_id": ObjectId("13a024fac8b4e6f8e98c8876"),
            "retweet_id": ObjectId("77153ab1e4ca26ebdaca2985")
        },
        {
            "_id": ObjectId("1c64bf8034356bee4079efd8"),
            "tweet_id": ObjectId("fa78002ff2e0db6c41d0dd98"),
            "retweet_id": ObjectId("5bb8b98d4cf6f3fb281757d7")
        },
        {
            "_id": ObjectId("d9d12b2d6616c506a5c411ec"),
            "tweet_id": ObjectId("f1719a2b4536ea8acd8cf0da"),
            "retweet_id": ObjectId("4d68b0044fa95f8b4bb20d76")
        },
        {
            "_id": ObjectId("b90785b6988ba553fc4a7385"),
            "tweet_id": ObjectId("6da54f6df6776857cf2c594a"),
            "retweet_id": ObjectId("4d9b402c6e4a51a5d5e17e3c")
        },
        {
            "_id": ObjectId("f88d9e517a7db2c71fc95b63"),
            "tweet_id": ObjectId("f6e6768cc24e7960a98682cf"),
            "retweet_id": ObjectId("4494b6b9007b314a941375aa")
        },
        {
            "_id": ObjectId("cff773475a72fbfaf222c652"),
            "tweet_id": ObjectId("6dc0323697969ae2ecaaec6e"),
            "retweet_id": ObjectId("4a9ca6575d5d61e555bde564")
        },
        {
            "_id": ObjectId("6382a80caa0635a34719c497"),
            "tweet_id": ObjectId("e590d7f48615b83461233676"),
            "retweet_id": ObjectId("f7b4246b693ea6426ec745f6")
        },
        {
            "_id": ObjectId("4cad9da98556011dde40017b"),
            "tweet_id": ObjectId("220d681ac8feb88f23a08fbf"),
            "retweet_id": ObjectId("0f7e8cd79b58b90ac1c41b03")
        },
        {
            "_id": ObjectId("b96556d074a4f050539a91b8"),
            "tweet_id": ObjectId("dfe325cf41632cd5e4f53457"),
            "retweet_id": ObjectId("ff083ed1c526792e0ee9288b")
        },
        {
            "_id": ObjectId("530e1a13443caf722e247812"),
            "tweet_id": ObjectId("dc94b08ce88bf32e8d9a37bf"),
            "retweet_id": ObjectId("eb7f1fa69995b98fc0bdf6c1")
        },
        {
            "_id": ObjectId("3e1f9ebcbf4186ec5eb7ea55"),
            "tweet_id": ObjectId("89e77dc3f053407d14f88cea"),
            "retweet_id": ObjectId("5e428f0ec78f2703ea817429")
        },
        {
            "_id": ObjectId("81205774051625401a2b22a1"),
            "tweet_id": ObjectId("f393c5854a72ff46c96c148f"),
            "retweet_id": ObjectId("c1f0a42bffee62bb5898e995")
        },
        {
            "_id": ObjectId("034d20f8dc7e78a06527de96"),
            "tweet_id": ObjectId("ded66c98f4b30bb8b8a8c64a"),
            "retweet_id": ObjectId("fcbfe972fae82c2384e7f984")
        },
        {
            "_id": ObjectId("1234136cc32e37a2435c39a6"),
            "tweet_id": ObjectId("ee856881a763a031699132ae"),
            "retweet_id": ObjectId("997c0531713cc39d2d7daeeb")
        },
        {
            "_id": ObjectId("72d6086eb8ee2b2cebaaa6a0"),
            "tweet_id": ObjectId("d51ab55a784f980211821ffa"),
            "retweet_id": ObjectId("b6bff2b2e8c9989ccbeb1a30")
        },
        {
            "_id": ObjectId("b22c86d95994dd49b5a48fc8"),
            "tweet_id": ObjectId("636913a10e06adf968e8ddc2"),
            "retweet_id": ObjectId("32e4da8f8f034a8b323937f4")
        },
        {
            "_id": ObjectId("0c2523d1ef7fa06c375ef005"),
            "tweet_id": ObjectId("35160afdb44c0c79a1149819"),
            "retweet_id": ObjectId("d397740a1ea634355338e76e")
        },
        {
            "_id": ObjectId("23d8c2dd111c0938a42bde40"),
            "tweet_id": ObjectId("0c8dfdb723691cc3ce1cb18a"),
            "retweet_id": ObjectId("6f0419c94bf7b408eb4c4b0e")
        },
        {
            "_id": ObjectId("29cf80b9d485cea050ac928d"),
            "tweet_id": ObjectId("08091df482c2d67061e598eb"),
            "retweet_id": ObjectId("a7a9c45b17fc37b7b1a4dc70")
        },
        {
            "_id": ObjectId("ddc74d3d1d6e281dcb41a0a4"),
            "tweet_id": ObjectId("e9c5955b9f07c565055bec13"),
            "retweet_id": ObjectId("83ecc862f0a4c4961331255f")
        },
        {
            "_id": ObjectId("bf6824710ab9d681df0b27d4"),
            "tweet_id": ObjectId("f104e1baf1ed7a821f273ef9"),
            "retweet_id": ObjectId("919cd39afbe07d0d15d45216")
        },
        {
            "_id": ObjectId("a7363dfcf997b9b80bf7d6f4"),
            "tweet_id": ObjectId("5fbf3b375df77b03b37e7222"),
            "retweet_id": ObjectId("52341fa64ac0a7c4d220a490")
        },
        {
            "_id": ObjectId("a7c5b3766bd482a72164868f"),
            "tweet_id": ObjectId("5d7858f8434f08fcb35b22da"),
            "retweet_id": ObjectId("4182d8393479856b769feb6a")
        },
        {
            "_id": ObjectId("212e3e9895e481e51aa6f984"),
            "tweet_id": ObjectId("89026485120406b6b3c49a83"),
            "retweet_id": ObjectId("a4a01ea371f663ae0ca7eca4")
        },
        {
            "_id": ObjectId("b2aa6584d67f68b576a97713"),
            "tweet_id": ObjectId("9766f4094358175d0011a766"),
            "retweet_id": ObjectId("0f9a5be884ad8d4ebd23fce6")
        },
        {
            "_id": ObjectId("e5a8824d50f18c3bf1d4ec61"),
            "tweet_id": ObjectId("d6f9336af994c09e2008d985"),
            "retweet_id": ObjectId("e844963413dab901b435a31e")
        },
        {
            "_id": ObjectId("e197f3331175d5470549055f"),
            "tweet_id": ObjectId("91d082805397f9fb2c9ab55a"),
            "retweet_id": ObjectId("b51e273784f789f5e6f6cb82")
        },
        {
            "_id": ObjectId("1d8b5f80917408c85fdd2779"),
            "tweet_id": ObjectId("aa3a26fbcdae909a87c9af9e"),
            "retweet_id": ObjectId("52f3b742a1a6bfbfa3ee9901")
        },
        {
            "_id": ObjectId("2a2f65a7e516265ee8eb2d8b"),
            "tweet_id": ObjectId("5308687b11ffdc08d5c22dc3"),
            "retweet_id": ObjectId("7ecc8655615d3da535d47d1d")
        },
        {
            "_id": ObjectId("643f02a1a5670c62666bab01"),
            "tweet_id": ObjectId("8e0714f49e946d22eb439193"),
            "retweet_id": ObjectId("5bdc1da36978ff56ed404590")
        },
        {
            "_id": ObjectId("8b5b72ca91287934660318df"),
            "tweet_id": ObjectId("7111febc22136513395a9b5b"),
            "retweet_id": ObjectId("e1e43b1046c22a3db4b5ef86")
        },
        {
            "_id": ObjectId("28f458ea5138f22833a1ce18"),
            "tweet_id": ObjectId("fc0fc09401b57b363cd72f9f"),
            "retweet_id": ObjectId("29891ced816558f254a5e655")
        },
        {
            "_id": ObjectId("4af6131ee0d2c7fc56995860"),
            "tweet_id": ObjectId("1a7274acf572e5aaf2466f67"),
            "retweet_id": ObjectId("18ff4ada13a33e1c03f373fc")
        },
        {
            "_id": ObjectId("eb2793765d2f384ff36a80be"),
            "tweet_id": ObjectId("27ce0888e09f2ed7f9de8c33"),
            "retweet_id": ObjectId("cbc49c73b22e495d77b34b9b")
        },
        {
            "_id": ObjectId("ed131642582cef73d08e1915"),
            "tweet_id": ObjectId("f5dee8f53fbf68d183a7ef52"),
            "retweet_id": ObjectId("5b07e812e548b51d2d9b16ae")
        },
        {
            "_id": ObjectId("57299826f6c089b718d25279"),
            "tweet_id": ObjectId("bcae52f94ee9786fc6abc5f2"),
            "retweet_id": ObjectId("78ea7a4ad7477dc289019fc5")
        },
        {
            "_id": ObjectId("d22d9f469c91d56fa5bc9de5"),
            "tweet_id": ObjectId("49fb7fb71f6fe4dd809edb97"),
            "retweet_id": ObjectId("ad92064c1130dd47ea98e423")
        },
        {
            "_id": ObjectId("23a5e4729aa620d159862405"),
            "tweet_id": ObjectId("a36d0e590ba7d5432b718ed0"),
            "retweet_id": ObjectId("7834576a821ded0da19132c5")
        },
        {
            "_id": ObjectId("052f12ab8b8ce58b6bf096e8"),
            "tweet_id": ObjectId("14ddd62054232baaba6c6f2f"),
            "retweet_id": ObjectId("83152e0e9b0377cafd11446c")
        },
        {
            "_id": ObjectId("419a9f844c4b37cee1c7d40e"),
            "tweet_id": ObjectId("977df546bee0b1949c55b63a"),
            "retweet_id": ObjectId("29c33bf243004375b7b071d4")
        },
        {
            "_id": ObjectId("7a0719e0cf86206e014bdcec"),
            "tweet_id": ObjectId("c1ea2e9ebade62f83e08b730"),
            "retweet_id": ObjectId("5b6375ce777ee7de4acd1590")
        },
        {
            "_id": ObjectId("5b3f5b82442677732c4ff4d3"),
            "tweet_id": ObjectId("afb6cfcb6517754f6e2441d9"),
            "retweet_id": ObjectId("0c45324338ce1abd8ad5ca43")
        },
        {
            "_id": ObjectId("55e68903342fc4e513a89981"),
            "tweet_id": ObjectId("d78c557d49d5ff2ec8a74a44"),
            "retweet_id": ObjectId("2b21fc934aa1ec980d7950da")
        },
        {
            "_id": ObjectId("794bb515df552e391f97a970"),
            "tweet_id": ObjectId("e3363b00f4f124522413069a"),
            "retweet_id": ObjectId("cecc4037c57b3a4241766336")
        },
        {
            "_id": ObjectId("98db6c0d0b6bfedb513456b5"),
            "tweet_id": ObjectId("91eda964264c6463974c4581"),
            "retweet_id": ObjectId("2e192b237d4daa90e289b42a")
        },
        {
            "_id": ObjectId("818366b78f4617c7d6f95a66"),
            "tweet_id": ObjectId("60b9239d0842241944cacd6d"),
            "retweet_id": ObjectId("2b21fc934aa1ec980d7950da")
        },
        {
            "_id": ObjectId("3087ce1ff294f03122f6de1d"),
            "tweet_id": ObjectId("26226a3e62205a9b4221c898"),
            "retweet_id": ObjectId("2fe4d8c0dc73eda397f0bc02")
        },
        {
            "_id": ObjectId("86348e6c1c16926ac0cd11a8"),
            "tweet_id": ObjectId("99c323be57a4bbca1534f614"),
            "retweet_id": ObjectId("bc27e6742fc88c0f4c487d7d")
        },
        {
            "_id": ObjectId("3c4cf0a05e8fcd88a0138d07"),
            "tweet_id": ObjectId("a8f92ec98f14da943748a7a0"),
            "retweet_id": ObjectId("fac99158282e50b084160db8")
        },
        {
            "_id": ObjectId("a0c303358089f2b07dd4510f"),
            "tweet_id": ObjectId("3d64ce2eb8f1906ece23f202"),
            "retweet_id": ObjectId("21c56c056ff9584f979a0882")
        },
        {
            "_id": ObjectId("78c54ef7f6aaa08392a4fb08"),
            "tweet_id": ObjectId("2bd686853fe77dc45d7c9048"),
            "retweet_id": ObjectId("70efe0a28664500cb09fb530")
        },
        {
            "_id": ObjectId("fb8f0dbedd6567e755dc00fd"),
            "tweet_id": ObjectId("a487496d2a08ceaec49564d1"),
            "retweet_id": ObjectId("10cffd39e1ec01c40b41e646")
        },
        {
            "_id": ObjectId("ae520a2d525a79401b03f097"),
            "tweet_id": ObjectId("1c93d2d6457c7d5b5a8f001c"),
            "retweet_id": ObjectId("d4ab427085852b006dba3452")
        },
        {
            "_id": ObjectId("21c0f00463a9a11d8283cf71"),
            "tweet_id": ObjectId("ee24d5637bf5771615d01a56"),
            "retweet_id": ObjectId("6edbd1bc76f354fa47a6255c")
        },
        {
            "_id": ObjectId("847be85c4f9e6b12d3b52782"),
            "tweet_id": ObjectId("d1299cd50dbef846e1411d7d"),
            "retweet_id": ObjectId("932b12a02bd22b04d5e33d29")
        },
        {
            "_id": ObjectId("6db3c65dc7755765d7ce502e"),
            "tweet_id": ObjectId("a2db61ccfd4b12b4d7be054f"),
            "retweet_id": ObjectId("1653ba58a94a1a56ba7beb12")
        },
        {
            "_id": ObjectId("dcb66becb22b4fbdde99b450"),
            "tweet_id": ObjectId("746275442f4508756b3a1208"),
            "retweet_id": ObjectId("fc1c00f346fc8904b2701305")
        },
        {
            "_id": ObjectId("9dc4b01612669b028d3a4c1f"),
            "tweet_id": ObjectId("077ad086278fb770a4f0995c"),
            "retweet_id": ObjectId("f3bcff12d60a23caeb1d98ff")
        },
        {
            "_id": ObjectId("820eca0e558396c70650b488"),
            "tweet_id": ObjectId("e68d06fe452b1e44268487d1"),
            "retweet_id": ObjectId("d06cfa74f65e127d2a310df4")
        },
        {
            "_id": ObjectId("b03ecab6d86ff54e18deb3d3"),
            "tweet_id": ObjectId("838885b1dcdb072b7954daed"),
            "retweet_id": ObjectId("f43c09251e57b6f1f48f18db")
        },
        {
            "_id": ObjectId("c750b1c650b82804dcc6bcc5"),
            "tweet_id": ObjectId("b57e6b8993ac26ca4c8a88a3"),
            "retweet_id": ObjectId("a92ca116269e90ff2fe6b0db")
        },
        {
            "_id": ObjectId("cfbabc59c91bd73d0915590b"),
            "tweet_id": ObjectId("f59a9b7524457bc76d469f71"),
            "retweet_id": ObjectId("38f37a53bf7c90a67d1ebaea")
        },
        {
            "_id": ObjectId("8358e27580bc8c10549b903c"),
            "tweet_id": ObjectId("131e209b6dd67af9c6191321"),
            "retweet_id": ObjectId("b0fdf28073bad0f3ca8ccf45")
        },
        {
            "_id": ObjectId("aa6566417e7ced6f18b11f17"),
            "tweet_id": ObjectId("d78c557d49d5ff2ec8a74a44"),
            "retweet_id": ObjectId("3c6f30fa17de9b055154acbb")
        },
        {
            "_id": ObjectId("7eb3c8a6fcce658757033141"),
            "tweet_id": ObjectId("c3e3f49a957a202f7aada602"),
            "retweet_id": ObjectId("20d70b2d8fae1faebfa9c7a2")
        },
        {
            "_id": ObjectId("f9408cd4782dd011c333bb60"),
            "tweet_id": ObjectId("811de275dea15811cfbdc322"),
            "retweet_id": ObjectId("967910f27ccffae027bcd079")
        },
        {
            "_id": ObjectId("c6bb45cb1e65fbd0d41901dd"),
            "tweet_id": ObjectId("997cc863f9adc7b1f2b3694f"),
            "retweet_id": ObjectId("4bec0deb848a8eb299fbd542")
        },
        {
            "_id": ObjectId("91570dd885aeff57a9d33af3"),
            "tweet_id": ObjectId("c9dfd67ea6cdbbb87134929d"),
            "retweet_id": ObjectId("92dfad881fb7df7f63f370a3")
        },
        {
            "_id": ObjectId("e20420345896a62bb79bc0d1"),
            "tweet_id": ObjectId("ef4dde8fd167fb94f27e7a94"),
            "retweet_id": ObjectId("2c4876b574dae7874b8849db")
        },
        {
            "_id": ObjectId("2cf450852ace281755849483"),
            "tweet_id": ObjectId("2b326a4a8fd0ed1df585a9b8"),
            "retweet_id": ObjectId("fb0cf9319fb44b9244e69305")
        },
        {
            "_id": ObjectId("4e789833ebc7278fd1e26c7c"),
            "tweet_id": ObjectId("119971fb86a79ff20b8998b7"),
            "retweet_id": ObjectId("20e91b417d8dd9edf42b7ec4")
        },
        {
            "_id": ObjectId("5d29e251476180f6b8709701"),
            "tweet_id": ObjectId("1c3509c28167bc306859fb1a"),
            "retweet_id": ObjectId("7a3b715474db7440481cfc4e")
        },
        {
            "_id": ObjectId("0e9f99c563f4e371836059f2"),
            "tweet_id": ObjectId("da16e53f95da77c204b268c7"),
            "retweet_id": ObjectId("2ed9b176f6652820a371a46a")
        },
        {
            "_id": ObjectId("4588e1cf3ad5edc782ebd667"),
            "tweet_id": ObjectId("018858cc17deb988a4cc6937"),
            "retweet_id": ObjectId("1e3a11405da5e7908e82b60b")
        },
        {
            "_id": ObjectId("8986a8036e0fd960936944b6"),
            "tweet_id": ObjectId("174b40d730970db60aa52a9e"),
            "retweet_id": ObjectId("cabf91e715ead6eabee80dbb")
        },
        {
            "_id": ObjectId("0af7fdae590dd5c443ad91b6"),
            "tweet_id": ObjectId("f42b996d4df7000563ab6a01"),
            "retweet_id": ObjectId("3fc78f63508c9d4dbfa0ccf4")
        },
        {
            "_id": ObjectId("a0bf5bf638b12bb95a838a2c"),
            "tweet_id": ObjectId("9b1aac17ac5a2216a102bc5b"),
            "retweet_id": ObjectId("e60e10e65c1f22c262d61e8a")
        },
        {
            "_id": ObjectId("9cb873b771d164a337e83770"),
            "tweet_id": ObjectId("1669dae448b9f28fb7b3f9d7"),
            "retweet_id": ObjectId("d167a3fa6ceeed40538aefe2")
        },
        {
            "_id": ObjectId("9577daaf1c7e2080d133fd54"),
            "tweet_id": ObjectId("dc8eb0e6c2e9867b54287cde"),
            "retweet_id": ObjectId("31991c4be8cc6243b86e37b9")
        },
        {
            "_id": ObjectId("de65fefcb94129c25abb582e"),
            "tweet_id": ObjectId("7ea52ee8ac3b74e19ca76ae1"),
            "retweet_id": ObjectId("b194acab81e2fad05d9e07e2")
        },
        {
            "_id": ObjectId("0f910f705e6bbfcf288f1ce7"),
            "tweet_id": ObjectId("4131a3246007363f738733a6"),
            "retweet_id": ObjectId("c01c90f3aa158d7729184fba")
        },
        {
            "_id": ObjectId("97067d55a701b0086c9c36a5"),
            "tweet_id": ObjectId("07a3580cbc067a4cb2d7ebc8"),
            "retweet_id": ObjectId("394c12f4a81d001610298f4e")
        },
        {
            "_id": ObjectId("2bdf2fe7f30ff05207ebf213"),
            "tweet_id": ObjectId("13baee513170bbead65b878c"),
            "retweet_id": ObjectId("ef4dde8fd167fb94f27e7a94")
        },
        {
            "_id": ObjectId("0757ecd4f949df44b4b92584"),
            "tweet_id": ObjectId("0eddd9863be3a2342e464927"),
            "retweet_id": ObjectId("f8704441cb337d04c2400458")
        },
        {
            "_id": ObjectId("98808b1234ce4a4cbf6336b6"),
            "tweet_id": ObjectId("d1e554713a89f239e1530241"),
            "retweet_id": ObjectId("507576899b03b6123347e2b3")
        },
        {
            "_id": ObjectId("5f3c6d8f3d2082d59a44eb8f"),
            "tweet_id": ObjectId("65c4bc8d71627fb8fe13ea2b"),
            "retweet_id": ObjectId("b5ff420aeaf77df8e96e2665")
        },
        {
            "_id": ObjectId("63be987d9d9e6445ed59ab7f"),
            "tweet_id": ObjectId("a9d8bef0d5886729ab8c8f19"),
            "retweet_id": ObjectId("940055c64608b967f137bccb")
        },
        {
            "_id": ObjectId("56a28aa2cef8af7d714c0a07"),
            "tweet_id": ObjectId("5f7762158cee356f96c66a97"),
            "retweet_id": ObjectId("9ba824af72ce874093ccfe3a")
        },
        {
            "_id": ObjectId("590c7e2869485699b9e7d13d"),
            "tweet_id": ObjectId("2427dfdce7b990a6a13e9d25"),
            "retweet_id": ObjectId("e88c5b7997005b6f45679697")
        },
        {
            "_id": ObjectId("02e21ce6d48d5892ab4237b5"),
            "tweet_id": ObjectId("9db9d08d0d84fc091795b33b"),
            "retweet_id": ObjectId("83108ddf44a4c87a867225a1")
        },
        {
            "_id": ObjectId("9f614ed1ad7fd49e936edcdf"),
            "tweet_id": ObjectId("f7d5576a31146d30d2b30791"),
            "retweet_id": ObjectId("82b2295827b5b9f034cc692e")
        },
        {
            "_id": ObjectId("d5a520b207d1b84e64f43ab3"),
            "tweet_id": ObjectId("a950af2208f8b90957dcca4a"),
            "retweet_id": ObjectId("7229566be5ea77540ea6f0f4")
        },
        {
            "_id": ObjectId("2426dea1ac6c4c9f2439658d"),
            "tweet_id": ObjectId("de7899492ee9e12bb466aee5"),
            "retweet_id": ObjectId("73e2a51357be1b69d7f81e72")
        },
        {
            "_id": ObjectId("c2b66be40838534924d8196a"),
            "tweet_id": ObjectId("8f39bc421bb2d574393faafa"),
            "retweet_id": ObjectId("a394cde00ca74a764e974698")
        },
        {
            "_id": ObjectId("436b3fde38cc595f923d4998"),
            "tweet_id": ObjectId("1f3c8218d03148b87844d961"),
            "retweet_id": ObjectId("e4d358e1ebacd652e2bc9e0e")
        },
        {
            "_id": ObjectId("8917d12d02f7dc7651615ab2"),
            "tweet_id": ObjectId("0d806d84bf9e350c127c6230"),
            "retweet_id": ObjectId("766f005bbf93bf352516917d")
        },
        {
            "_id": ObjectId("4902bdb1c4fb9c7984b40f0e"),
            "tweet_id": ObjectId("6aa962ed6d303c3c74bd99bb"),
            "retweet_id": ObjectId("3bf4d041464a0266852d7cc9")
        },
        {
            "_id": ObjectId("2dbdb65650211e56f7a8e8db"),
            "tweet_id": ObjectId("d00f2e3c4a8d7c03a185f6b0"),
            "retweet_id": ObjectId("f4a3e6af7502d1e55d495932")
        },
        {
            "_id": ObjectId("6726754e7b0c89684ee1b146"),
            "tweet_id": ObjectId("57f727dd69813dc361a531c7"),
            "retweet_id": ObjectId("f3898a96cb1fe80b070b5ce8")
        },
        {
            "_id": ObjectId("44bb42c987155467122e3d91"),
            "tweet_id": ObjectId("60e18fc07cff63a58486ee92"),
            "retweet_id": ObjectId("5d4e4847fd518e121b178053")
        },
        {
            "_id": ObjectId("2b5132d7bc566bfcaf891af9"),
            "tweet_id": ObjectId("c498bf9568d11f3d063a472a"),
            "retweet_id": ObjectId("41268540ed30ca9ee0aec5f7")
        },
        {
            "_id": ObjectId("1ec5fd2f759a28dea17d8fdc"),
            "tweet_id": ObjectId("18aadb41587a40706820ee53"),
            "retweet_id": ObjectId("1ce22613f63f853d8ec570a5")
        },
        {
            "_id": ObjectId("d7dd66a3a150c5d5c6346c72"),
            "tweet_id": ObjectId("bc93a2fc2233ba9804ab61ed"),
            "retweet_id": ObjectId("df3fa914eb13114cd1f542fe")
        },
        {
            "_id": ObjectId("9f8e61fc8b93e962dae715f9"),
            "tweet_id": ObjectId("800dd3a5bc082f3e91aad6da"),
            "retweet_id": ObjectId("9f885772edeb193b3382e6e8")
        },
        {
            "_id": ObjectId("d8123b24eb87194fe371297d"),
            "tweet_id": ObjectId("166fdf4dfbb203d242964258"),
            "retweet_id": ObjectId("d535e734fdacc41a6a4113db")
        },
        {
            "_id": ObjectId("9816bd13cac2c90e0b7aed6b"),
            "tweet_id": ObjectId("9e4cd93c9614a5295ac4374e"),
            "retweet_id": ObjectId("045c54a6a0b6ddb9b83b8c30")
        },
        {
            "_id": ObjectId("21467583f69797e67e2b8d79"),
            "tweet_id": ObjectId("8f2f995f89be66865710144f"),
            "retweet_id": ObjectId("e91ea18d0640c0db18cbcccb")
        },
        {
            "_id": ObjectId("2179c52627498f3f697f426b"),
            "tweet_id": ObjectId("6bdc747a69faaded84eaaac5"),
            "retweet_id": ObjectId("81880226e567494426afe051")
        },
        {
            "_id": ObjectId("f8577f05951ea67e583a0faa"),
            "tweet_id": ObjectId("a7c0738746389a5b8bd1d282"),
            "retweet_id": ObjectId("823e7c4d6d75c046a0a0d0d7")
        },
        {
            "_id": ObjectId("01509cad903597f1656e3974"),
            "tweet_id": ObjectId("dd1f17eff09ae83d153cb71d"),
            "retweet_id": ObjectId("d185c29b46ad427f3a82c5b8")
        },
        {
            "_id": ObjectId("7066e6f4a326966a6da55b09"),
            "tweet_id": ObjectId("3a7f4fd20de66374b06f380f"),
            "retweet_id": ObjectId("115950ba139e6d6bf11dc5b6")
        },
        {
            "_id": ObjectId("73d35172b0063f4e62ee50bb"),
            "tweet_id": ObjectId("cda9e3a6ed07ae1c0eb9e7ad"),
            "retweet_id": ObjectId("2952f787b5a93ac888c2bdf0")
        },
        {
            "_id": ObjectId("c77c31dbc2fd0ed033b436ce"),
            "tweet_id": ObjectId("5e5cda8de9635d64452d31a1"),
            "retweet_id": ObjectId("85968c7a027ccbcd365fd848")
        },
        {
            "_id": ObjectId("ca7ae707eb17bfe34093b6d1"),
            "tweet_id": ObjectId("8273d75109a64f913eb5f1e9"),
            "retweet_id": ObjectId("e02a2c26aa3b42da07572a7c")
        },
        {
            "_id": ObjectId("5bb6f83faabf636b36957cb2"),
            "tweet_id": ObjectId("315f1ec661afc7b727092637"),
            "retweet_id": ObjectId("a3369474be1d17fe48fb86a6")
        },
        {
            "_id": ObjectId("7f43389964cfc06421c3efa1"),
            "tweet_id": ObjectId("073dc1631e780055d712fcba"),
            "retweet_id": ObjectId("480594b7e6aede09392ac977")
        },
        {
            "_id": ObjectId("ee687b64c3bc7b4a574a8798"),
            "tweet_id": ObjectId("cbf36e6d161faae81d5e9520"),
            "retweet_id": ObjectId("596eb53ca211e35867114646")
        },
        {
            "_id": ObjectId("a23cc49e208f8896a47d5f3a"),
            "tweet_id": ObjectId("f9ec4badc29a91b291458eac"),
            "retweet_id": ObjectId("6e3252eb90abf0ff2d7c9604")
        },
        {
            "_id": ObjectId("c8739bf71e57a36060172f12"),
            "tweet_id": ObjectId("a10ba28867ae8a12d1265a01"),
            "retweet_id": ObjectId("6e2c8379ef20e10d5aa9b572")
        },
        {
            "_id": ObjectId("1b5b7e1d7eb170bd80f7a552"),
            "tweet_id": ObjectId("b72cc0ea7939a4911bb33fca"),
            "retweet_id": ObjectId("357847802ef110a513704b91")
        },
        {
            "_id": ObjectId("ac0d07a8b97f80e94a33ff84"),
            "tweet_id": ObjectId("ab5586567a5bc72e13024aef"),
            "retweet_id": ObjectId("65e924bd4c9bf9635fa171af")
        },
        {
            "_id": ObjectId("2f36c8039279bd39d90c2748"),
            "tweet_id": ObjectId("461347072864d532d37b4039"),
            "retweet_id": ObjectId("66f6091826bc95ac578b0291")
        },
        {
            "_id": ObjectId("b18b69c9e80a1925b8735502"),
            "tweet_id": ObjectId("5bcbd88400b6f4eb5b520832"),
            "retweet_id": ObjectId("7871c00dfe98704c25196e68")
        },
        {
            "_id": ObjectId("78e793e352f3287ba7a5a8a7"),
            "tweet_id": ObjectId("469e27e25287ecabdef02295"),
            "retweet_id": ObjectId("4965d761b6ddf9156173a521")
        },
        {
            "_id": ObjectId("729abea6507ac9aa3a9fc97c"),
            "tweet_id": ObjectId("aee0f5facec7c1136cdbb483"),
            "retweet_id": ObjectId("380f4380548dfb76aa50c9eb")
        },
        {
            "_id": ObjectId("6f87764aeccf225a7f6db919"),
            "tweet_id": ObjectId("603c1eff20a14046651817b8"),
            "retweet_id": ObjectId("a88cf5895bff604b24cbf37a")
        },
        {
            "_id": ObjectId("e96dbc28445c5125027faaab"),
            "tweet_id": ObjectId("32e0411175363db34f3cd50c"),
            "retweet_id": ObjectId("78b3d1208b214815c1d1193d")
        },
        {
            "_id": ObjectId("3efc465f22e5164c251d57de"),
            "tweet_id": ObjectId("7e5b8a86a7ce776428aeefda"),
            "retweet_id": ObjectId("1e7f829fa0db7c02fc959ca5")
        },
        {
            "_id": ObjectId("287749aa246df74e81cdfec4"),
            "tweet_id": ObjectId("69dbdce98748af7319428620"),
            "retweet_id": ObjectId("e2543f1af934ebee49acdad1")
        },
        {
            "_id": ObjectId("fb9c5c2d7462e50164a0102f"),
            "tweet_id": ObjectId("beadf8b0cc1e38aabaa47a7a"),
            "retweet_id": ObjectId("c2937481d2e60bd00af6b060")
        },
        {
            "_id": ObjectId("cdf8f0794ebf50317819dfe9"),
            "tweet_id": ObjectId("f8e4a25681dcb9c7be0d2256"),
            "retweet_id": ObjectId("8692e1a48bbc67637aa9926c")
        },
        {
            "_id": ObjectId("c9d4958c94405f4d10696102"),
            "tweet_id": ObjectId("bc9168d50124716f3f7fd2b9"),
            "retweet_id": ObjectId("44526302a2f27ae63dd2c88d")
        },
        {
            "_id": ObjectId("a2f8e917a7af689e4eb9c3ae"),
            "tweet_id": ObjectId("a86c7f397b1d7b1299d9dd42"),
            "retweet_id": ObjectId("69be3a5c414e7767312be6ea")
        },
        {
            "_id": ObjectId("63028c64aa67b02d9d80892e"),
            "tweet_id": ObjectId("b6a170e786ae64a21ec4be06"),
            "retweet_id": ObjectId("015216b18d52e8c6508bfa3e")
        },
        {
            "_id": ObjectId("98fb720ba53385e3e6f4d8bf"),
            "tweet_id": ObjectId("668a7205c167eed57868094d"),
            "retweet_id": ObjectId("281d2b8b6e667049c03bb5aa")
        },
        {
            "_id": ObjectId("486214c89ab04d77af6faadd"),
            "tweet_id": ObjectId("b1cb96b0c6458df1dbb72055"),
            "retweet_id": ObjectId("0a7bb0624d442effc84599f2")
        },
        {
            "_id": ObjectId("15677fd8fb3223801d1eb00f"),
            "tweet_id": ObjectId("50136f54b3d37c2b7e66f9b8"),
            "retweet_id": ObjectId("fd97c999acbb266cfa487141")
        },
        {
            "_id": ObjectId("a3fa29feedca752f81253d8f"),
            "tweet_id": ObjectId("f3421ae1a77c8b3f1401bdf0"),
            "retweet_id": ObjectId("6c2ba13e42226269f237b850")
        },
        {
            "_id": ObjectId("40e1c4491fc9d3e39e5ee6c9"),
            "tweet_id": ObjectId("36f28160da2b6c245a31a0b3"),
            "retweet_id": ObjectId("45d882195746171cbb3ca9e3")
        },
        {
            "_id": ObjectId("99a40dde524ed396c5755fad"),
            "tweet_id": ObjectId("fc6ebd714e69a94c574c42c9"),
            "retweet_id": ObjectId("7970b65a523264fc9193b1d5")
        },
        {
            "_id": ObjectId("5721b083f2226754f9cd7d62"),
            "tweet_id": ObjectId("d204145ff086b923c3342c47"),
            "retweet_id": ObjectId("a393dc62184ce26cd3e147c3")
        },
        {
            "_id": ObjectId("3e5bb88f610d883ee01e976b"),
            "tweet_id": ObjectId("b1707f67361f257a4732a786"),
            "retweet_id": ObjectId("a5431166741d018e766cef6a")
        },
        {
            "_id": ObjectId("e2905693dffacbd4d0679fb9"),
            "tweet_id": ObjectId("f0c257959f93c606569c80cf"),
            "retweet_id": ObjectId("2427dfdce7b990a6a13e9d25")
        },
        {
            "_id": ObjectId("00709c0077fad6176e09e76f"),
            "tweet_id": ObjectId("8ddb8905ee1d623e265e6fcb"),
            "retweet_id": ObjectId("fcb84b4464b3c3967c1f52d1")
        },
        {
            "_id": ObjectId("8e1f7f647c8a8902a85dc35a"),
            "tweet_id": ObjectId("81880226e567494426afe051"),
            "retweet_id": ObjectId("d5ea0d2351f02a9d3572f367")
        },
        {
            "_id": ObjectId("b3aea0b11ce3e883f318fab7"),
            "tweet_id": ObjectId("388c0cffba55b59fd59fa8d7"),
            "retweet_id": ObjectId("7dac9858ceb0a60e346ba5d6")
        },
        {
            "_id": ObjectId("a8ffb28d96702a38b88245d9"),
            "tweet_id": ObjectId("366c79225dbe5aece420ba17"),
            "retweet_id": ObjectId("d78c557d49d5ff2ec8a74a44")
        },
        {
            "_id": ObjectId("66b12ce3efa73f9514aecf97"),
            "tweet_id": ObjectId("f3bcff12d60a23caeb1d98ff"),
            "retweet_id": ObjectId("9e3c85b076407ce5e3793158")
        },
        {
            "_id": ObjectId("9730f1a3bf4694121728dac2"),
            "tweet_id": ObjectId("06ed118eaf3b637a0b548d0b"),
            "retweet_id": ObjectId("52e29e3981e9cc3a8121e107")
        },
        {
            "_id": ObjectId("f3e03857deab12f7bbd71aef"),
            "tweet_id": ObjectId("517241743fcbfe7ac6147ab0"),
            "retweet_id": ObjectId("8e991f45a2a9471454a9bcfb")
        },
        {
            "_id": ObjectId("fef1cf00da33e7bcbec78670"),
            "tweet_id": ObjectId("2058f2cf6e37e23457a45472"),
            "retweet_id": ObjectId("633565dad57b62ce2c98f18d")
        },
        {
            "_id": ObjectId("e04eaa568d47f4167f631af4"),
            "tweet_id": ObjectId("7ea888573f438ebd183e8327"),
            "retweet_id": ObjectId("bd8afe527615e313b32d680b")
        },
        {
            "_id": ObjectId("8c18a6d6284bcd838b625d05"),
            "tweet_id": ObjectId("b330d2c2be796d7180f056ce"),
            "retweet_id": ObjectId("f5753d906e1c9d0dd881ca06")
        },
        {
            "_id": ObjectId("5d8b3b1a4daf808ca797e521"),
            "tweet_id": ObjectId("81d3046db4b391ab1490ceb1"),
            "retweet_id": ObjectId("966c9b399488e6d43526f136")
        },
        {
            "_id": ObjectId("4d20c87ee1ebadc97004ef4a"),
            "tweet_id": ObjectId("fc5bdb6c9ed5ef92fd3c7973"),
            "retweet_id": ObjectId("6475c81f1cd34dded124ea61")
        },
        {
            "_id": ObjectId("776903f2c9bdb646fc81239d"),
            "tweet_id": ObjectId("e35a3a85336aedf95ea8d6d1"),
            "retweet_id": ObjectId("01a0856e6cb8510de4de5e7f")
        },
        {
            "_id": ObjectId("410df1dc5fffcfcc0147ef35"),
            "tweet_id": ObjectId("43946716740a0cc78e473b4a"),
            "retweet_id": ObjectId("57a8a4b38d0d8ffb66a9c33b")
        },
        {
            "_id": ObjectId("3b29ccd21beea3bdaddf9f49"),
            "tweet_id": ObjectId("f326a05f2b13c4faca47648c"),
            "retweet_id": ObjectId("0f35aec79c72dd1ba1349af4")
        },
        {
            "_id": ObjectId("b509e03efdbdc00036ebed3f"),
            "tweet_id": ObjectId("5e5cda8de9635d64452d31a1"),
            "retweet_id": ObjectId("290e5797c1b3db07c73d2bcf")
        },
        {
            "_id": ObjectId("ef92856badac7553ce253cd1"),
            "tweet_id": ObjectId("f3421ae1a77c8b3f1401bdf0"),
            "retweet_id": ObjectId("9aab959fd2ff4937d0f29d78")
        },
        {
            "_id": ObjectId("0348493d23b2ecaf5ccb6edc"),
            "tweet_id": ObjectId("b0effa7b09e36f5e533653f1"),
            "retweet_id": ObjectId("f0b9ccebdf298aef84a1d9d7")
        },
        {
            "_id": ObjectId("726c893d9d9f8697dc6a1a0e"),
            "tweet_id": ObjectId("e7084145b23fbae875a3efc0"),
            "retweet_id": ObjectId("cedff1399c0e41202bbc8f8c")
        },
        {
            "_id": ObjectId("fd764658ddf05f8412c359d2"),
            "tweet_id": ObjectId("bb289ffb5ab562b08dac8736"),
            "retweet_id": ObjectId("59707cbd97dd57bb649af354")
        },
        {
            "_id": ObjectId("6cdf8012b57e18b4417fb8eb"),
            "tweet_id": ObjectId("246e1b700881fcf46cfab090"),
            "retweet_id": ObjectId("6f4487e0c3653aac94e944cf")
        },
        {
            "_id": ObjectId("91caafb917d8d2febf891b11"),
            "tweet_id": ObjectId("a9c40c2337226dfbeb9dc597"),
            "retweet_id": ObjectId("fcb84b4464b3c3967c1f52d1")
        },
        {
            "_id": ObjectId("3f03babd644574bf3bdb6f55"),
            "tweet_id": ObjectId("c6e3786006016d8ebba985ae"),
            "retweet_id": ObjectId("70ec44b35051db9cada13275")
        },
        {
            "_id": ObjectId("40e1d323370b270adf0cac1d"),
            "tweet_id": ObjectId("07d9c7f099e1fde59c3df84a"),
            "retweet_id": ObjectId("30ed546cec1bf3877839c113")
        },
        {
            "_id": ObjectId("61fb8e5707379364673c11f8"),
            "tweet_id": ObjectId("18e98d71097e0a0d6c046f9a"),
            "retweet_id": ObjectId("50ef5543d0a1d933840f1b37")
        },
        {
            "_id": ObjectId("c5d4d10c37392123b537e9cb"),
            "tweet_id": ObjectId("fe3616ae1718ed29125c85df"),
            "retweet_id": ObjectId("947925f478e46850175c4c29")
        },
        {
            "_id": ObjectId("0b2e952e861bd15167c11d34"),
            "tweet_id": ObjectId("f60c836691d02593d311d987"),
            "retweet_id": ObjectId("40e6bd221857e93ca5470fbf")
        },
        {
            "_id": ObjectId("5d0d4af6015d964a98095992"),
            "tweet_id": ObjectId("b944fee7bb391256738d4d31"),
            "retweet_id": ObjectId("4c111571192ac57eacf3f7f2")
        },
        {
            "_id": ObjectId("4565ef16626f25d110520f14"),
            "tweet_id": ObjectId("ff5721af7ab34e72178ab067"),
            "retweet_id": ObjectId("997cc863f9adc7b1f2b3694f")
        },
        {
            "_id": ObjectId("8064b105cb5427940af0c50e"),
            "tweet_id": ObjectId("f06663205cfc8d9fe6f93dad"),
            "retweet_id": ObjectId("5110f99c4450d0c008b8356f")
        },
        {
            "_id": ObjectId("34c7ac47f4af5bb36ced5716"),
            "tweet_id": ObjectId("739feba495afa5f8c7503619"),
            "retweet_id": ObjectId("d5f85f4b2200b30d8af3ab93")
        },
        {
            "_id": ObjectId("45ca961bf97691b6efd6a011"),
            "tweet_id": ObjectId("ce15e3e4b071631dfeef3f9c"),
            "retweet_id": ObjectId("31f0cbe15d8864309b864faa")
        },
        {
            "_id": ObjectId("f484fc6ef29e9afddb80b192"),
            "tweet_id": ObjectId("7f063091fc02bfae42c00970"),
            "retweet_id": ObjectId("7aec2207df12f236feade27d")
        },
        {
            "_id": ObjectId("c126d08da51c95024ae2281e"),
            "tweet_id": ObjectId("930e11d6eab8f3e30eecb8a4"),
            "retweet_id": ObjectId("ab130a2b0640efeb6d524fc7")
        },
        {
            "_id": ObjectId("49edc9126d69496c68c4d082"),
            "tweet_id": ObjectId("b6b9e372192bb6c55e1e6b6e"),
            "retweet_id": ObjectId("e7ac5f890cfb4d1789bf9a11")
        },
        {
            "_id": ObjectId("9b8877e1cbdbda4d3c5793cc"),
            "tweet_id": ObjectId("66150256b645744e36232528"),
            "retweet_id": ObjectId("b72b96efd853c9f75d834bbf")
        },
        {
            "_id": ObjectId("e1e15ce6ea91f2da8d779c7a"),
            "tweet_id": ObjectId("27db45da8474b60c8efb2307"),
            "retweet_id": ObjectId("51c6f1a7e47a94920dc54a8e")
        },
        {
            "_id": ObjectId("6868b3ab3af6121e200dd69c"),
            "tweet_id": ObjectId("b1599ecb6d4e26eff8a04e17"),
            "retweet_id": ObjectId("11388b1be5baf487854d9ffc")
        },
        {
            "_id": ObjectId("901637af333062c1663910d4"),
            "tweet_id": ObjectId("5d251e8adb7a486f81186c23"),
            "retweet_id": ObjectId("d29a3f883b27998d9bfa79e5")
        },
        {
            "_id": ObjectId("0f54a2173a1969b59fbcefba"),
            "tweet_id": ObjectId("8e26a3de9bd86d7177b1b5ac"),
            "retweet_id": ObjectId("3dc16bb1add30a2ec1074a42")
        },
        {
            "_id": ObjectId("7ee8185983485b4a5949f8aa"),
            "tweet_id": ObjectId("332a3f6f980b1d0f5ab899ba"),
            "retweet_id": ObjectId("f4cb47d46bbc8acbfe30b5e9")
        },
        {
            "_id": ObjectId("52f561ec897b3806130a5a65"),
            "tweet_id": ObjectId("b9ec3a0255ccebc99415af6d"),
            "retweet_id": ObjectId("847f1d1ceda9598f91a95b4b")
        },
        {
            "_id": ObjectId("fb607040fae3f17af9d284f1"),
            "tweet_id": ObjectId("96c58f8ac569ab216d304639"),
            "retweet_id": ObjectId("adaaf0337da342259e2e6a3f")
        },
        {
            "_id": ObjectId("2c600a92ab0b516d00770552"),
            "tweet_id": ObjectId("3a9d5b065e2bbad7f0f88869"),
            "retweet_id": ObjectId("7b119800e3201b6bcca43744")
        },
        {
            "_id": ObjectId("930d27bd284e555690f424c9"),
            "tweet_id": ObjectId("39d51a2b5022870895e6d73e"),
            "retweet_id": ObjectId("cc5c4d1d3e828718a9252542")
        },
        {
            "_id": ObjectId("c45ebf5b55d73d3de11aa8da"),
            "tweet_id": ObjectId("d2ed8738b6db06e8975896e8"),
            "retweet_id": ObjectId("a29a1a940c5c6621b2fd40e8")
        },
        {
            "_id": ObjectId("9b41a77b177860160c5dcb0b"),
            "tweet_id": ObjectId("c04078082cfabb42ae22e125"),
            "retweet_id": ObjectId("0981dd4d298d85fba3417a07")
        },
        {
            "_id": ObjectId("4aca1de31375fbbd69d28237"),
            "tweet_id": ObjectId("0a602e6c0fa2333f7435e693"),
            "retweet_id": ObjectId("248892abcf6064cb87f0fc7f")
        },
        {
            "_id": ObjectId("e831aad18769ab66dd8d10ed"),
            "tweet_id": ObjectId("8273d75109a64f913eb5f1e9"),
            "retweet_id": ObjectId("920c193d4da34bbf25f1787f")
        },
        {
            "_id": ObjectId("45874600e2ed081bd9053009"),
            "tweet_id": ObjectId("7c4a73c49d74384d7fc6b030"),
            "retweet_id": ObjectId("9a18a464fc7cb8beab7c119e")
        },
        {
            "_id": ObjectId("5496291f82d2fcb584db750c"),
            "tweet_id": ObjectId("642fa2deef7eb073d121eea6"),
            "retweet_id": ObjectId("831d0139a49e7af4237e9352")
        },
        {
            "_id": ObjectId("8128c8aa1e83c44d736e6124"),
            "tweet_id": ObjectId("9e0923546b3985f6bc4bb995"),
            "retweet_id": ObjectId("adaaf0337da342259e2e6a3f")
        },
        {
            "_id": ObjectId("b885de02e32def2fcf30132f"),
            "tweet_id": ObjectId("bb28b852e99d987b4ef85e7d"),
            "retweet_id": ObjectId("ea53e45dd1c91b5e1c6dceb1")
        },
        {
            "_id": ObjectId("4499fef67bf0691ab4e6e9b9"),
            "tweet_id": ObjectId("d069df0f93b4991720b012ee"),
            "retweet_id": ObjectId("6464ce2b29a66bf58e19d06e")
        },
        {
            "_id": ObjectId("460e2e7339d60ea9c89cb54b"),
            "tweet_id": ObjectId("6d344d44f8cd0660cc7f41ed"),
            "retweet_id": ObjectId("f9ec4badc29a91b291458eac")
        },
        {
            "_id": ObjectId("7a7861dc867c05fa9b0b2659"),
            "tweet_id": ObjectId("2ca0966d3a9783aa928ec3c0"),
            "retweet_id": ObjectId("73e6d6014514f7f1ade557d7")
        },
        {
            "_id": ObjectId("e533e8ae1f510d2bee7d775a"),
            "tweet_id": ObjectId("c87b3477c83aafe3cefacaff"),
            "retweet_id": ObjectId("633fb538bb653581b2f001e9")
        },
        {
            "_id": ObjectId("21149bf4721c9f7d206a20ac"),
            "tweet_id": ObjectId("d8c701d5d6572c8637909803"),
            "retweet_id": ObjectId("1ce22613f63f853d8ec570a5")
        },
        {
            "_id": ObjectId("60bb6eb3662f4fa81feb714f"),
            "tweet_id": ObjectId("5d9e77626060e367a5392304"),
            "retweet_id": ObjectId("8b8b2fd9890871be0ae66e59")
        },
        {
            "_id": ObjectId("acc01cd97ffa8a1856d58c92"),
            "tweet_id": ObjectId("55bde90f68711f48f674d140"),
            "retweet_id": ObjectId("3c576b09525afc3ba892db31")
        },
        {
            "_id": ObjectId("f954a1debf3dcbb208c7ad20"),
            "tweet_id": ObjectId("a1b7c210bfe78867b932f7e9"),
            "retweet_id": ObjectId("bc91b37f65d674eff6406403")
        },
        {
            "_id": ObjectId("30ea2b9ae2c54cfbe582c903"),
            "tweet_id": ObjectId("79e8fee1feaf6c9bfe716f4d"),
            "retweet_id": ObjectId("868bc79f732906956282e125")
        },
        {
            "_id": ObjectId("e41cbbaf44d40ad67c6f8482"),
            "tweet_id": ObjectId("99751123e5b87d1a1f8e7042"),
            "retweet_id": ObjectId("cc155e13b273cba5a2696894")
        },
        {
            "_id": ObjectId("a3bdd05e2f9c496586e7b5d2"),
            "tweet_id": ObjectId("4c8d49f923c53a65ef18adbe"),
            "retweet_id": ObjectId("3825dc60d0812ded400c546d")
        },
        {
            "_id": ObjectId("b1a9ece58a92cf1cf71624e6"),
            "tweet_id": ObjectId("1831dae5d0f9a90f8c7a6c79"),
            "retweet_id": ObjectId("400e5b2fa2a1b89330e2a487")
        },
        {
            "_id": ObjectId("9bba0202bd09d3bcbe38e74f"),
            "tweet_id": ObjectId("a5c3e791ace5724b8eeacf82"),
            "retweet_id": ObjectId("b06f7eb48ec0ef921459a6da")
        },
        {
            "_id": ObjectId("df1ebae8f06932cd8769c582"),
            "tweet_id": ObjectId("0583872f907fd98bd112e0da"),
            "retweet_id": ObjectId("500ab09054a14d9f069478ee")
        },
        {
            "_id": ObjectId("1fc8bb3a2316d8c05016796c"),
            "tweet_id": ObjectId("cbf426b8f0efcabb5e4174a5"),
            "retweet_id": ObjectId("34d9a8d8d75422f14d75f5d1")
        },
        {
            "_id": ObjectId("cb766654403676cc47a6185a"),
            "tweet_id": ObjectId("2d28fa5635d990bf28b4f7c2"),
            "retweet_id": ObjectId("11a7499217b0f69c301a440c")
        },
        {
            "_id": ObjectId("4d7d7506e75ea975d447be88"),
            "tweet_id": ObjectId("31de78cda2897c452053bd55"),
            "retweet_id": ObjectId("eb525443ae0eab94e19f0391")
        },
        {
            "_id": ObjectId("8032694b39d6932df010a0ee"),
            "tweet_id": ObjectId("4ffb433eba021265ad23d9ba"),
            "retweet_id": ObjectId("a936eba5fd9282f8fadef631")
        },
        {
            "_id": ObjectId("3dabc08962c3b318a9995051"),
            "tweet_id": ObjectId("076f602cfec64955501056a8"),
            "retweet_id": ObjectId("165a6354b1c7342fc3d83557")
        },
        {
            "_id": ObjectId("1049aeb190e473f4593d4fbc"),
            "tweet_id": ObjectId("17a51280cd461f1fc31c5fd8"),
            "retweet_id": ObjectId("facb144813abf723dddeabf7")
        },
        {
            "_id": ObjectId("870f1d64393eeb0bff82e731"),
            "tweet_id": ObjectId("9dc75c417319df55bfbb4d70"),
            "retweet_id": ObjectId("53382f3ed7916140288171b5")
        },
        {
            "_id": ObjectId("eb20aba36d10df47b5a30ae7"),
            "tweet_id": ObjectId("f3bcff12d60a23caeb1d98ff"),
            "retweet_id": ObjectId("7edd05b727db6839c0ef639a")
        },
        {
            "_id": ObjectId("91e3f6383e0b0feac7db1fcd"),
            "tweet_id": ObjectId("f90e58d1262561a1a15a4a63"),
            "retweet_id": ObjectId("93c2204d96be8e4f1d3eef34")
        },
        {
            "_id": ObjectId("63f24b43123b5334752d5241"),
            "tweet_id": ObjectId("efb3d2b112a67e64ba4ad47e"),
            "retweet_id": ObjectId("07e76f60583e65c3b519c33f")
        },
        {
            "_id": ObjectId("3d77cd8046f4f55f68ca6d33"),
            "tweet_id": ObjectId("80e7365c380b7d0964382db3"),
            "retweet_id": ObjectId("1dfd94fd755252209c2acf70")
        },
        {
            "_id": ObjectId("daaa7c786120c82cc3c84391"),
            "tweet_id": ObjectId("6099b3a5453ce032e180c720"),
            "retweet_id": ObjectId("68b43063d2d7d5ba5961462e")
        },
        {
            "_id": ObjectId("83d36fb88b7d8865f8f659a6"),
            "tweet_id": ObjectId("7a3b715474db7440481cfc4e"),
            "retweet_id": ObjectId("d8b27296257e60606e784ebc")
        },
        {
            "_id": ObjectId("6ba6e4764535e01f14cd2b57"),
            "tweet_id": ObjectId("6b940b6d777f0d2a254d9b33"),
            "retweet_id": ObjectId("148d3edc09ccc128e159c544")
        },
        {
            "_id": ObjectId("aeeec1e012b5d6dff637d150"),
            "tweet_id": ObjectId("6319c7eba15829f40aa2c8d3"),
            "retweet_id": ObjectId("27323cf1b26be18f69644e88")
        },
        {
            "_id": ObjectId("4cd20113f47547d154a295a2"),
            "tweet_id": ObjectId("5d530df190441a1107d8dd1f"),
            "retweet_id": ObjectId("f0c257959f93c606569c80cf")
        },
        {
            "_id": ObjectId("af74cebf6d782fa1c0672603"),
            "tweet_id": ObjectId("65e95d99fc377ebf673c972d"),
            "retweet_id": ObjectId("39ce057b3d89c7d0133fd56a")
        },
        {
            "_id": ObjectId("1f66474c5038db11b7e8d34a"),
            "tweet_id": ObjectId("9c6536954ad210461e27aa6e"),
            "retweet_id": ObjectId("a62cdf37df04f4f196ee9eab")
        },
        {
            "_id": ObjectId("21861d4d3546056e02dc3811"),
            "tweet_id": ObjectId("c613a34c430a6fc7012b17d7"),
            "retweet_id": ObjectId("b497799c272ec5d894fb09be")
        },
        {
            "_id": ObjectId("464c498276f2bec69507b298"),
            "tweet_id": ObjectId("efbbd3650a5c1f7db8b5d6cf"),
            "retweet_id": ObjectId("be1cb4c4478d08dfb0757a9d")
        },
        {
            "_id": ObjectId("8511ba9c46fb990de4e6d584"),
            "tweet_id": ObjectId("f744a895fc448eeb90a175b1"),
            "retweet_id": ObjectId("8697985d4bfc018c1bf32e01")
        },
        {
            "_id": ObjectId("98f723f59938d8f56030e29a"),
            "tweet_id": ObjectId("160c7bcab983ba402efd1366"),
            "retweet_id": ObjectId("49491f33723a0a8bf73b86c6")
        },
        {
            "_id": ObjectId("04677d7c012250ca6ea424e0"),
            "tweet_id": ObjectId("5ba7b2976e5e00ecfb032351"),
            "retweet_id": ObjectId("f709067624ab387dc681cfd6")
        },
        {
            "_id": ObjectId("3c81fe97431c64b04133592a"),
            "tweet_id": ObjectId("e809e6df5c4124c2a23aa3ea"),
            "retweet_id": ObjectId("f7fbb27c063915eab9f11037")
        },
        {
            "_id": ObjectId("915316828401c7a69bb62cf5"),
            "tweet_id": ObjectId("5c4fb1e9367dc350328d4da5"),
            "retweet_id": ObjectId("451a1b9977c87a9a08432543")
        },
        {
            "_id": ObjectId("29b4d0dc83bb3c8c831b3ffa"),
            "tweet_id": ObjectId("6a10f17420b156de111ccb3b"),
            "retweet_id": ObjectId("50978fc359f5701d55af8bde")
        },
        {
            "_id": ObjectId("f120d18cb5fc4be8140ddbe9"),
            "tweet_id": ObjectId("2f471022eec9dcf68f13a97c"),
            "retweet_id": ObjectId("2da4053e5eac705ae26f6f26")
        },
        {
            "_id": ObjectId("2774835473787d7c918f887b"),
            "tweet_id": ObjectId("37a5fe5ce8877ea482598a86"),
            "retweet_id": ObjectId("4736891c1b597ad73b09381d")
        },
        {
            "_id": ObjectId("cc225715c4bff050d9e68ead"),
            "tweet_id": ObjectId("2f03c45a4004455ea9856d4f"),
            "retweet_id": ObjectId("c260a999f2725c0917711eb0")
        },
        {
            "_id": ObjectId("6a57508b18eaf40839dc466a"),
            "tweet_id": ObjectId("de3fe2538c280611d5f921b2"),
            "retweet_id": ObjectId("865e58c3780a58da10d18bf8")
        },
        {
            "_id": ObjectId("063064b8e6be96d599594973"),
            "tweet_id": ObjectId("a88cf5895bff604b24cbf37a"),
            "retweet_id": ObjectId("2630ad5198ec070d7e87d6c4")
        },
        {
            "_id": ObjectId("64e7dfab2dfe9bcbecc99f94"),
            "tweet_id": ObjectId("c080230b50234c9c27c1e2f6"),
            "retweet_id": ObjectId("945a1786d94e0f86e261d5ce")
        },
        {
            "_id": ObjectId("a23497bd2d8b1f54787de9ae"),
            "tweet_id": ObjectId("b3c09f439b83a76762f32aa3"),
            "retweet_id": ObjectId("c7feb464bf08e359af63357f")
        },
        {
            "_id": ObjectId("5afc2c1126b763b41fb74fb2"),
            "tweet_id": ObjectId("4ea47d72466eb44ad0fff45f"),
            "retweet_id": ObjectId("f03f06a7d2bd62ac7522c9e7")
        },
        {
            "_id": ObjectId("a9fc721b3e7e1f5f39c3293b"),
            "tweet_id": ObjectId("79e8fee1feaf6c9bfe716f4d"),
            "retweet_id": ObjectId("3de5a34b6b03a869d798b212")
        },
        {
            "_id": ObjectId("922eca0ac92e2287bb71370b"),
            "tweet_id": ObjectId("a22871de6bf9089ee1f92a5a"),
            "retweet_id": ObjectId("b3c09f439b83a76762f32aa3")
        },
        {
            "_id": ObjectId("3ccf3c334ba5c5fef54f8a00"),
            "tweet_id": ObjectId("b1b7ca33698bc24fa7d670bf"),
            "retweet_id": ObjectId("b119c7a8e2f27d589273bf27")
        },
        {
            "_id": ObjectId("1b36dfa01f4773291ae11c36"),
            "tweet_id": ObjectId("9761ad149f193744a88bd240"),
            "retweet_id": ObjectId("ac5fa5b1a0caa9417ef2ab79")
        },
        {
            "_id": ObjectId("c812864e4f7815868a79732c"),
            "tweet_id": ObjectId("7daf50fc3e78585e19aae5ce"),
            "retweet_id": ObjectId("c7e425ee974a05919b528a13")
        },
        {
            "_id": ObjectId("0bab4b0c0351b31c78ccc03a"),
            "tweet_id": ObjectId("b35ffa4875befde2b8ffa159"),
            "retweet_id": ObjectId("4f44ea032210cd60631e66ee")
        },
        {
            "_id": ObjectId("1eb04b79224f02567926fb60"),
            "tweet_id": ObjectId("8bf86c563fd3a76a4c013ed8"),
            "retweet_id": ObjectId("68b7d117fa32a486b1e75fa8")
        },
        {
            "_id": ObjectId("9a466b751e7e95592ee41938"),
            "tweet_id": ObjectId("985f00e9ddf73d5df5999d1d"),
            "retweet_id": ObjectId("930e11d6eab8f3e30eecb8a4")
        },
        {
            "_id": ObjectId("4f4c26a3e8f799e2f36326b7"),
            "tweet_id": ObjectId("73e23c5f54448c6ead98958f"),
            "retweet_id": ObjectId("794ed506636d2e788f2cf1d7")
        },
        {
            "_id": ObjectId("9cf783011c705f5176cc583e"),
            "tweet_id": ObjectId("2afdac65fb2d8d6aeaad84f6"),
            "retweet_id": ObjectId("aecac89734f3b7d6199e4399")
        },
        {
            "_id": ObjectId("20e846609ea46e3604b66c38"),
            "tweet_id": ObjectId("8a4ad84b1f1344da0c1b60ac"),
            "retweet_id": ObjectId("8b41278f00ab768dd30df7e3")
        },
        {
            "_id": ObjectId("4366e9429d76b9c0ee4bc3cd"),
            "tweet_id": ObjectId("a9c40c2337226dfbeb9dc597"),
            "retweet_id": ObjectId("cb96371c90cd5e2bd1f8d421")
        },
        {
            "_id": ObjectId("83202098b0d7c902c3107c44"),
            "tweet_id": ObjectId("868bc79f732906956282e125"),
            "retweet_id": ObjectId("b66893096d9cb617a9f4f096")
        },
        {
            "_id": ObjectId("95f4d31c94bbe6a1af6f769e"),
            "tweet_id": ObjectId("ba92b25200588117a0f6d7b4"),
            "retweet_id": ObjectId("cb96371c90cd5e2bd1f8d421")
        },
        {
            "_id": ObjectId("b19efd2f32ef6f1737ba692f"),
            "tweet_id": ObjectId("a9c40c2337226dfbeb9dc597"),
            "retweet_id": ObjectId("a3473c77046717ebb649ff15")
        },
        {
            "_id": ObjectId("1ed1d0433e7b8d8e49cf51c1"),
            "tweet_id": ObjectId("27db45da8474b60c8efb2307"),
            "retweet_id": ObjectId("22a1c17b0ca1e58218582f55")
        },
        {
            "_id": ObjectId("c41d2f6f28838b10384f95ad"),
            "tweet_id": ObjectId("805cd3af0932be4da7d71e30"),
            "retweet_id": ObjectId("eafd87fd291638e38f619bf2")
        },
        {
            "_id": ObjectId("5a2420b68a13b1035cf97a18"),
            "tweet_id": ObjectId("0e372d17125d8d4d0f2338cf"),
            "retweet_id": ObjectId("2263f837629e7e0a53343127")
        },
        {
            "_id": ObjectId("eb7aa2d2efcf9614fa420b49"),
            "tweet_id": ObjectId("201f8e6305ab30903c7429ad"),
            "retweet_id": ObjectId("160c7bcab983ba402efd1366")
        },
        {
            "_id": ObjectId("9f19fe9c93a4db605c800aec"),
            "tweet_id": ObjectId("69efc9e62618d12a3cd14d8d"),
            "retweet_id": ObjectId("4017f663e7a64202adc98bbc")
        },
        {
            "_id": ObjectId("2a4a8177ab012de9c1101145"),
            "tweet_id": ObjectId("c1d41e08f5239fbe936cd594"),
            "retweet_id": ObjectId("e381a7fce144b1a8007d30ca")
        },
        {
            "_id": ObjectId("d9e8f56fc18ab5cec3484e79"),
            "tweet_id": ObjectId("b775ffab7ba7558281cd7470"),
            "retweet_id": ObjectId("92dfad881fb7df7f63f370a3")
        },
        {
            "_id": ObjectId("81ae8dd46f47ffaa4769c94c"),
            "tweet_id": ObjectId("f0b8d7163de745dc162e2871"),
            "retweet_id": ObjectId("73396873e4d0145e134d1d9d")
        },
        {
            "_id": ObjectId("8db05bd48765b13c9a0054e1"),
            "tweet_id": ObjectId("d8b27296257e60606e784ebc"),
            "retweet_id": ObjectId("36eb194e2c98fb030477e0d4")
        },
        {
            "_id": ObjectId("62e6e6cfae7cdfa3f78c62aa"),
            "tweet_id": ObjectId("c71298a6f58f5c79c9662c77"),
            "retweet_id": ObjectId("df8043027efed6ec78144b0c")
        },
        {
            "_id": ObjectId("ae1fa22297cfe23d5e6fc5e6"),
            "tweet_id": ObjectId("bad51c15d81c30f9074f653e"),
            "retweet_id": ObjectId("ec394fa00289619cd67dc69d")
        },
        {
            "_id": ObjectId("073217b9adcc599f3f14e910"),
            "tweet_id": ObjectId("8e0fd8d664aff3ed7934abc4"),
            "retweet_id": ObjectId("1bbfb7c80fc19d10ae8d90ee")
        },
        {
            "_id": ObjectId("f90f3fb1e3591e64458c2d26"),
            "tweet_id": ObjectId("7eb9c9c3fedeac0be5612db8"),
            "retweet_id": ObjectId("4c5f1dfcbcf6c0fb8b77035a")
        },
        {
            "_id": ObjectId("0ef12f53dea0161286705f7a"),
            "tweet_id": ObjectId("ec394fa00289619cd67dc69d"),
            "retweet_id": ObjectId("37141e5dc4f8dba8195e2f15")
        },
        {
            "_id": ObjectId("86fae74e82aded496b4a3617"),
            "tweet_id": ObjectId("f592b5a89cc9371f82a62dd5"),
            "retweet_id": ObjectId("b97ebd1f4f2d2f2ccf01c2f3")
        },
        {
            "_id": ObjectId("7f3aec29409b3cc42d73e48b"),
            "tweet_id": ObjectId("157daaa5bf869d961934f1d2"),
            "retweet_id": ObjectId("cedff1399c0e41202bbc8f8c")
        },
        {
            "_id": ObjectId("35c3f25ec76af3ef365f6691"),
            "tweet_id": ObjectId("7888f012fb6fa1926762c3ff"),
            "retweet_id": ObjectId("0cbda5a1b85d352c28511231")
        },
        {
            "_id": ObjectId("e5d32bdb8dd94b23374cacf5"),
            "tweet_id": ObjectId("3ecc8187d74d0c3f0355f73e"),
            "retweet_id": ObjectId("f87f459bab6e1f688047cbdf")
        },
        {
            "_id": ObjectId("a063733f64343607f6e4c1b8"),
            "tweet_id": ObjectId("80e067c4639d93679180910b"),
            "retweet_id": ObjectId("8730ffe7242f541884ba1697")
        },
        {
            "_id": ObjectId("e880fe68602d1f5d0ed2b173"),
            "tweet_id": ObjectId("50978fc359f5701d55af8bde"),
            "retweet_id": ObjectId("8a1612551e2eddca4a3afb4d")
        },
        {
            "_id": ObjectId("6dd0fae84fe81497aef381df"),
            "tweet_id": ObjectId("42711d07b860bf193e768f4d"),
            "retweet_id": ObjectId("72bedbe76f730c94bf04b999")
        },
        {
            "_id": ObjectId("290f614c4de00f6b2b7a77b8"),
            "tweet_id": ObjectId("aea586cf66fd6f7365049517"),
            "retweet_id": ObjectId("987c22c90b2e1dddcbdce3d3")
        },
        {
            "_id": ObjectId("86eb1618294ed074d40ef1cc"),
            "tweet_id": ObjectId("e5889ff0117cadf9f436b912"),
            "retweet_id": ObjectId("c9723563d194688af14264ff")
        },
        {
            "_id": ObjectId("0783b18d79a61000dfd2a7ec"),
            "tweet_id": ObjectId("2d7b8fcc888b16e30ad8e28a"),
            "retweet_id": ObjectId("a989ee0a5ba8159c1cba12e2")
        },
        {
            "_id": ObjectId("156bd00ed6fc92e7215fbe24"),
            "tweet_id": ObjectId("2ca0966d3a9783aa928ec3c0"),
            "retweet_id": ObjectId("434711f54fa74482efaa817c")
        },
        {
            "_id": ObjectId("45b84c3a684e9988449f338a"),
            "tweet_id": ObjectId("b775ffab7ba7558281cd7470"),
            "retweet_id": ObjectId("246e1b700881fcf46cfab090")
        },
        {
            "_id": ObjectId("4505da4b0aff4a7e3caf6cb5"),
            "tweet_id": ObjectId("792ff1eb1756b45c502e8576"),
            "retweet_id": ObjectId("4fe4d72e4a6982106d046d0a")
        },
        {
            "_id": ObjectId("7168c07dfc6c835d56cb55eb"),
            "tweet_id": ObjectId("0a903954524828a4c115a86a"),
            "retweet_id": ObjectId("7111febc22136513395a9b5b")
        },
        {
            "_id": ObjectId("d3824ee868346b5beef1b0e4"),
            "tweet_id": ObjectId("c64c30e95c4c041732707508"),
            "retweet_id": ObjectId("21d475ff66f3063239a46da2")
        },
        {
            "_id": ObjectId("386c7f33c24ca6641bd8d3ef"),
            "tweet_id": ObjectId("7c2ff3f76eaeccb5b5a09b51"),
            "retweet_id": ObjectId("2d48bb610a789240dcfda0e8")
        },
        {
            "_id": ObjectId("6cc0a5295df5eaca04561f02"),
            "tweet_id": ObjectId("d204145ff086b923c3342c47"),
            "retweet_id": ObjectId("ee331b3dfb59b13d8d371532")
        },
        {
            "_id": ObjectId("850404f5c4130465cafb095f"),
            "tweet_id": ObjectId("e110c6121a24bf624d6ef50b"),
            "retweet_id": ObjectId("4bee97b951cd211da26fb16a")
        },
        {
            "_id": ObjectId("03016f8a1389f64d0af56d76"),
            "tweet_id": ObjectId("8e48f3d2df0a808382823e0f"),
            "retweet_id": ObjectId("e2f129601fdd7eccdd05e97d")
        },
        {
            "_id": ObjectId("dbb7899da8fecd6193953b18"),
            "tweet_id": ObjectId("2624c3446d156774a7c36293"),
            "retweet_id": ObjectId("71fd851f3594e99c84753ae1")
        },
        {
            "_id": ObjectId("63001370690245d10cde808c"),
            "tweet_id": ObjectId("c94d8a8ea458737188573a20"),
            "retweet_id": ObjectId("4d9b402c6e4a51a5d5e17e3c")
        },
        {
            "_id": ObjectId("ca1a613b9d8f9c938595884f"),
            "tweet_id": ObjectId("e4f5583d20659e7afd39e0dc"),
            "retweet_id": ObjectId("eb9d5724e1bef7ba466de494")
        },
        {
            "_id": ObjectId("ae29d422437cb2d5a90059c1"),
            "tweet_id": ObjectId("8b86115c3a60ee781243b5d0"),
            "retweet_id": ObjectId("d78c557d49d5ff2ec8a74a44")
        },
        {
            "_id": ObjectId("7764e89c1913e4e46850f750"),
            "tweet_id": ObjectId("91cfb8d8b98b25e21ba9dbd9"),
            "retweet_id": ObjectId("5605059f95e79b443bff40f4")
        },
        {
            "_id": ObjectId("b2cecd89d11957449bb6de20"),
            "tweet_id": ObjectId("4e33e77f20a62ff71aae9ece"),
            "retweet_id": ObjectId("70ec44b35051db9cada13275")
        },
        {
            "_id": ObjectId("2986dc383c57b7f3438509b7"),
            "tweet_id": ObjectId("0da930c8c4efe718f97b4a1e"),
            "retweet_id": ObjectId("4faf61c4f947d67e5a414878")
        },
        {
            "_id": ObjectId("d780f68634822155a6e02834"),
            "tweet_id": ObjectId("a296f7f2655670298ccc760e"),
            "retweet_id": ObjectId("f53768fc866a264b5c34c169")
        },
        {
            "_id": ObjectId("1a58473a7f09d9a681094ace"),
            "tweet_id": ObjectId("b7eb9a5426e8f606dca165c1"),
            "retweet_id": ObjectId("3bd2ccc5035bcab324609d97")
        },
        {
            "_id": ObjectId("6bc98e7668c1014df9fdc6a5"),
            "tweet_id": ObjectId("23f4a3803a65fb603f1a9575"),
            "retweet_id": ObjectId("573a8a2fdd08b1807235a91a")
        },
        {
            "_id": ObjectId("2127ae1a1a079f20117bb34e"),
            "tweet_id": ObjectId("2630ad5198ec070d7e87d6c4"),
            "retweet_id": ObjectId("1585164396ab152b18e4337c")
        },
        {
            "_id": ObjectId("9a5371018a8bd141643823cb"),
            "tweet_id": ObjectId("82cb34c801d6d0d5c7132cbc"),
            "retweet_id": ObjectId("8b866a486e06048d390239a0")
        },
        {
            "_id": ObjectId("aa2b738093b6e5e226adf638"),
            "tweet_id": ObjectId("c6eed65c364a51d339d8b16b"),
            "retweet_id": ObjectId("f91fba1d28ff4aaa90f9090f")
        },
        {
            "_id": ObjectId("63bf6b9da31630818d0485a3"),
            "tweet_id": ObjectId("97c700b0dddad5750994e68e"),
            "retweet_id": ObjectId("1b6b9260bae2ca84efb9d811")
        },
        {
            "_id": ObjectId("7b3a9808b4c7b1b793fabe56"),
            "tweet_id": ObjectId("c7d491aaaef964dcbf4751f7"),
            "retweet_id": ObjectId("713e738be7ea4f2e9a679b8e")
        },
        {
            "_id": ObjectId("46909619cf358687c3e6d7ac"),
            "tweet_id": ObjectId("ac0cf1f326c6da6bdec26509"),
            "retweet_id": ObjectId("c4fa4316ff1c0a728d6598d1")
        },
        {
            "_id": ObjectId("61d2c8e92d81c4f3401d9626"),
            "tweet_id": ObjectId("8714c2f440e429033992a568"),
            "retweet_id": ObjectId("1cb055cc1367444af900f004")
        },
        {
            "_id": ObjectId("9660c1b6b19d131ec8c31093"),
            "tweet_id": ObjectId("badeef6d845295133db8193a"),
            "retweet_id": ObjectId("19ad99f2a97c0a1e48cb749f")
        },
        {
            "_id": ObjectId("7f9ea970b4ce385bc22a3176"),
            "tweet_id": ObjectId("eafe95e2813beb87192fc679"),
            "retweet_id": ObjectId("ace32c19e536e71da4711162")
        },
        {
            "_id": ObjectId("1368af9d9bea19e4ae297eaa"),
            "tweet_id": ObjectId("debe8a48a43c0b5329c9c33c"),
            "retweet_id": ObjectId("a40cb80a4b4ad628e1af8c0c")
        },
        {
            "_id": ObjectId("41a3ae1e0cb1e9a810d1f751"),
            "tweet_id": ObjectId("d4e29f626faf45ebcfc509b1"),
            "retweet_id": ObjectId("394c12f4a81d001610298f4e")
        },
        {
            "_id": ObjectId("fdbbe216dd49fa541f1da614"),
            "tweet_id": ObjectId("71b56701ae9e42225f6ee7b9"),
            "retweet_id": ObjectId("b7facd08fe71e2240c5fab11")
        },
        {
            "_id": ObjectId("1bfe41e9fd48a3a663c88a63"),
            "tweet_id": ObjectId("852a2f1943a142b50279587f"),
            "retweet_id": ObjectId("0d3bc2dc8370f266612a18b9")
        },
        {
            "_id": ObjectId("cf31a876a9451e14d5c34a41"),
            "tweet_id": ObjectId("4b1912d080f3f622719d2b31"),
            "retweet_id": ObjectId("6b2d9a958c69e57834959261")
        },
        {
            "_id": ObjectId("a26cb00e0cc51daac85bec5c"),
            "tweet_id": ObjectId("2c4876b574dae7874b8849db"),
            "retweet_id": ObjectId("e6b22822a5f57345255b7af2")
        },
        {
            "_id": ObjectId("279544bd14bba4381b8f185b"),
            "tweet_id": ObjectId("aec57084bf77f3c3674c1314"),
            "retweet_id": ObjectId("3b89c0b659830bfa279a63ff")
        },
        {
            "_id": ObjectId("bd23b0078be49c71d60933db"),
            "tweet_id": ObjectId("57c4559fc85246b49d274b90"),
            "retweet_id": ObjectId("65e95d99fc377ebf673c972d")
        },
        {
            "_id": ObjectId("37350412f1b57e751f5ec109"),
            "tweet_id": ObjectId("eab105ed681c35b86e2d31f3"),
            "retweet_id": ObjectId("37122ecf2514749d937c9515")
        },
        {
            "_id": ObjectId("746a42e302bf52956c96c6db"),
            "tweet_id": ObjectId("994f426b595c6a34a03066d6"),
            "retweet_id": ObjectId("7bb57203cdbc931f971f5bd4")
        },
        {
            "_id": ObjectId("f5c3e67fdf429f86266d7cb3"),
            "tweet_id": ObjectId("a0e6c9b61d7e4cb8a1b029a8"),
            "retweet_id": ObjectId("d8812441d09b820a76f64c31")
        },
        {
            "_id": ObjectId("67a17f796b9e1359733e38de"),
            "tweet_id": ObjectId("d2929c114309124e9a561c10"),
            "retweet_id": ObjectId("449ea4b4f23a08cfc449fcf5")
        },
        {
            "_id": ObjectId("fb370c064b0d44aca7a9ecc7"),
            "tweet_id": ObjectId("563e11289e180c057b2106a4"),
            "retweet_id": ObjectId("ee49f07edab365dbb2fbecd8")
        },
        {
            "_id": ObjectId("4f04b5588e90d116125ad5af"),
            "tweet_id": ObjectId("f39e8984f46e7e8ebf049e6d"),
            "retweet_id": ObjectId("efc8cc5e69fb9313d5150f18")
        },
        {
            "_id": ObjectId("74dca6d685f6c70932db3a0e"),
            "tweet_id": ObjectId("fb1dd6424f52adcd40825341"),
            "retweet_id": ObjectId("06d261d8ab5d1dd29bad9c75")
        },
        {
            "_id": ObjectId("ef28157a53c488b397d4594d"),
            "tweet_id": ObjectId("7c0603897f5c418e08171fd6"),
            "retweet_id": ObjectId("c3a5beb31231d28f750bc6ca")
        },
        {
            "_id": ObjectId("3aae2ec24d4e9f5064c66586"),
            "tweet_id": ObjectId("e52449d824003fab745cfeeb"),
            "retweet_id": ObjectId("cf284d0fb388d51b4b6931f2")
        },
        {
            "_id": ObjectId("57cd07e462d39043fd5fc3f7"),
            "tweet_id": ObjectId("5dbbaa564e4241bcde4a8584"),
            "retweet_id": ObjectId("def182b51737cd8e3d1ccf74")
        },
        {
            "_id": ObjectId("70793676e8f470b989e5ef1c"),
            "tweet_id": ObjectId("5507babea14d6c73f27ca390"),
            "retweet_id": ObjectId("4efcf437bd3dfd7189e94f15")
        },
        {
            "_id": ObjectId("d1ab8f73037ad739931cfa0b"),
            "tweet_id": ObjectId("07b1c60ae89ab8a154b4545b"),
            "retweet_id": ObjectId("e3e453386beaf49c87d8b5c7")
        },
        {
            "_id": ObjectId("5e8a036f4f04e964b3c75586"),
            "tweet_id": ObjectId("71e68ebd537492fdff2c71d9"),
            "retweet_id": ObjectId("77153ab1e4ca26ebdaca2985")
        },
        {
            "_id": ObjectId("c6bf51f15056abc59756f1a9"),
            "tweet_id": ObjectId("a43e18403404a9c5ef43a57b"),
            "retweet_id": ObjectId("4ae8184a696acd801bc979c3")
        },
        {
            "_id": ObjectId("4bf1879c0d328323be30be42"),
            "tweet_id": ObjectId("59a92418fe9da8d8bf31f5dd"),
            "retweet_id": ObjectId("aebf2b788e0d1e31f720f735")
        },
        {
            "_id": ObjectId("58e9129a08e237666aa0a772"),
            "tweet_id": ObjectId("471ff3d01cccce04beea805b"),
            "retweet_id": ObjectId("0dce424a53567745e890b535")
        },
        {
            "_id": ObjectId("ff71c186afbedbb8c67e5aaa"),
            "tweet_id": ObjectId("2afdac65fb2d8d6aeaad84f6"),
            "retweet_id": ObjectId("9cd731475b465d7a4f1d7cfe")
        },
        {
            "_id": ObjectId("ae0c05adcf271bea87998cf7"),
            "tweet_id": ObjectId("a88cf5895bff604b24cbf37a"),
            "retweet_id": ObjectId("d397740a1ea634355338e76e")
        },
        {
            "_id": ObjectId("634d15ac1a33c23d6f27b6be"),
            "tweet_id": ObjectId("893a16bb138087b2dc03dd56"),
            "retweet_id": ObjectId("58dad67fc32e0e9c1050a433")
        },
        {
            "_id": ObjectId("047f17d708a5f4a4b758e897"),
            "tweet_id": ObjectId("e6b3c0cbd0a2996c4c2f3615"),
            "retweet_id": ObjectId("c8c75cd669b015a584e5faa3")
        },
        {
            "_id": ObjectId("01189ba31e19d1061c289961"),
            "tweet_id": ObjectId("e381a7fce144b1a8007d30ca"),
            "retweet_id": ObjectId("bbcc58d10c21d6f9e67dfcb2")
        },
        {
            "_id": ObjectId("28bd98644c35e081f62c68b4"),
            "tweet_id": ObjectId("659b3c19743472868cc077cd"),
            "retweet_id": ObjectId("8816c71b5fe4d24bbc2cdbfa")
        },
        {
            "_id": ObjectId("46587c52fe182fbe3b8825a8"),
            "tweet_id": ObjectId("852bdbe31d5f18e607d4acdd"),
            "retweet_id": ObjectId("0d1496c2ae2544842639e462")
        },
        {
            "_id": ObjectId("ff83bea0107859e142b2fe44"),
            "tweet_id": ObjectId("8390639448a6679afb773383"),
            "retweet_id": ObjectId("3d665593d4f80fa006e83445")
        },
        {
            "_id": ObjectId("9a7587a48650cc0dd59d63d9"),
            "tweet_id": ObjectId("a72d03a5b197b9a386486b67"),
            "retweet_id": ObjectId("6e49fbfce275fbcbbbf9e7e7")
        },
        {
            "_id": ObjectId("15268d6cf8569d4bb7209283"),
            "tweet_id": ObjectId("420bd9c23dd803daa6a99c13"),
            "retweet_id": ObjectId("6392eea8f7815c7a65f599bb")
        },
        {
            "_id": ObjectId("259651915ba2897b07d4044d"),
            "tweet_id": ObjectId("7ca9dd0c3b81f01dd14c97f6"),
            "retweet_id": ObjectId("c0357475b6c5954805dbbf4b")
        },
        {
            "_id": ObjectId("2dfbc6d9f9139b97a82d837c"),
            "tweet_id": ObjectId("912c22e92e754ca8af588bd5"),
            "retweet_id": ObjectId("705efa1a8a800b699068b0f8")
        },
        {
            "_id": ObjectId("f3ec1291abb5e48ed6f6b18c"),
            "tweet_id": ObjectId("da6decf4f125dd43a1a1ef0d"),
            "retweet_id": ObjectId("131b64405de7f975dc004f11")
        },
        {
            "_id": ObjectId("1a9b4780e75fb2a70ca17e23"),
            "tweet_id": ObjectId("f1df9b098c3aeac6a2651b66"),
            "retweet_id": ObjectId("bcc3adb59f9c4c25f4f2e7a8")
        },
        {
            "_id": ObjectId("e895544d80ebd4e314ab98bf"),
            "tweet_id": ObjectId("cf0728709f489b3b6203c5e0"),
            "retweet_id": ObjectId("ec518033e92c2f4f490f391e")
        },
        {
            "_id": ObjectId("a8d78a2c989d7528548c0485"),
            "tweet_id": ObjectId("69efc9e62618d12a3cd14d8d"),
            "retweet_id": ObjectId("8a1612551e2eddca4a3afb4d")
        },
        {
            "_id": ObjectId("f54d24ee1a8e7a714499bb31"),
            "tweet_id": ObjectId("057daddd04942202b28dc949"),
            "retweet_id": ObjectId("2d9e7107a07fca4960e53c88")
        },
        {
            "_id": ObjectId("680633b2d6e5b188c1bec02b"),
            "tweet_id": ObjectId("14ddd62054232baaba6c6f2f"),
            "retweet_id": ObjectId("7580fceb5a0964c32a5804a5")
        },
        {
            "_id": ObjectId("ca47eda0bc9a1d52b3086e49"),
            "tweet_id": ObjectId("269c484c170f24cb9ef5c8ed"),
            "retweet_id": ObjectId("cac555013500cd9ecec5e5e7")
        },
        {
            "_id": ObjectId("0b55eacffb18cabe8c8f9587"),
            "tweet_id": ObjectId("ed50c3c94b9e447ce74cfde7"),
            "retweet_id": ObjectId("7ea888573f438ebd183e8327")
        },
        {
            "_id": ObjectId("7a46abcf4ac28d5061fcd472"),
            "tweet_id": ObjectId("5be33e3ca1f90bf720e3897e"),
            "retweet_id": ObjectId("43ff6fa37dc01473d38e979b")
        },
        {
            "_id": ObjectId("e21ce3b7fe96dce4d4cf83dc"),
            "tweet_id": ObjectId("0d909ab54b0b6df6de4109f6"),
            "retweet_id": ObjectId("efd858c3c7a5bcf14968427b")
        },
        {
            "_id": ObjectId("51ac8cacdefe29b8d5ba51dd"),
            "tweet_id": ObjectId("d5fe7d30ec8ea803ef1e8038"),
            "retweet_id": ObjectId("2058f2cf6e37e23457a45472")
        },
        {
            "_id": ObjectId("65212c621488c2b35d0203f5"),
            "tweet_id": ObjectId("3098c4fc06159891b6e35772"),
            "retweet_id": ObjectId("1c44ff8edb43bdf51e6e3c3e")
        },
        {
            "_id": ObjectId("605277a1259223a714d411a5"),
            "tweet_id": ObjectId("caf65a3ecdb23b6db75cfcb5"),
            "retweet_id": ObjectId("478001fc450c5d2c3d987fd1")
        },
        {
            "_id": ObjectId("96c382d6711c880b3939949d"),
            "tweet_id": ObjectId("267f5e098c9373d58d2f426a"),
            "retweet_id": ObjectId("b0c558b54de0c9a8d95368ee")
        },
        {
            "_id": ObjectId("25030a48897b08f4d6299fba"),
            "tweet_id": ObjectId("9ad62beda3f939586b0bd15f"),
            "retweet_id": ObjectId("c08babae008393879f19f144")
        },
        {
            "_id": ObjectId("7665a7ea98398afaf9134a77"),
            "tweet_id": ObjectId("c7da2a2907d169324af2b2a7"),
            "retweet_id": ObjectId("87ee3e32fd22dad0360a406a")
        },
        {
            "_id": ObjectId("f768f9e61a13377de0dae516"),
            "tweet_id": ObjectId("8c819b088dff3fa1ca0a4d1c"),
            "retweet_id": ObjectId("143c9559f498344e2277ef3a")
        },
        {
            "_id": ObjectId("c9729e563dfb3c147573878c"),
            "tweet_id": ObjectId("67767a4ffa2934897466d2ed"),
            "retweet_id": ObjectId("cbc21dc37cfca00e389d0cc6")
        },
        {
            "_id": ObjectId("ea77dbf254cb60c7349fb263"),
            "tweet_id": ObjectId("18100ff2f9ce20c7bf5251f7"),
            "retweet_id": ObjectId("73e2a51357be1b69d7f81e72")
        },
        {
            "_id": ObjectId("56b23b121517b9d465114313"),
            "tweet_id": ObjectId("cabf91e715ead6eabee80dbb"),
            "retweet_id": ObjectId("dc99eb9f7fe4e8e91cdec982")
        },
        {
            "_id": ObjectId("0b32dcaa831290de4853a90e"),
            "tweet_id": ObjectId("5cfcb84b3924b0ba2b1c8a11"),
            "retweet_id": ObjectId("51c6f1a7e47a94920dc54a8e")
        },
        {
            "_id": ObjectId("e35ba03f95730c00732edac8"),
            "tweet_id": ObjectId("e55afb99dbd26ce2927dfc42"),
            "retweet_id": ObjectId("5f29505bdf8d6b383fea3caf")
        },
        {
            "_id": ObjectId("8027230ffa11970baead7900"),
            "tweet_id": ObjectId("9169a1c396840aa1957febe1"),
            "retweet_id": ObjectId("b8dbc30f98601ee66969cfa7")
        },
        {
            "_id": ObjectId("32e8fc72e5a94cdf39beef9d"),
            "tweet_id": ObjectId("ed35e2166953c60d50bae12a"),
            "retweet_id": ObjectId("b5fe4fade7641835dabb77cf")
        },
        {
            "_id": ObjectId("1b522e88ae5b6a518a178cc4"),
            "tweet_id": ObjectId("76d693563b48bec47f481450"),
            "retweet_id": ObjectId("c2937481d2e60bd00af6b060")
        },
        {
            "_id": ObjectId("c6209c7a6bd8a65c2f854fa5"),
            "tweet_id": ObjectId("65ef92ea158257349d4b83a1"),
            "retweet_id": ObjectId("95135cf41f7a0a2673efbeb7")
        },
        {
            "_id": ObjectId("99f8b4129fd55678dc785efb"),
            "tweet_id": ObjectId("dd0c18d7d50b97163b6ea98c"),
            "retweet_id": ObjectId("886d0488322563f9379081b5")
        },
        {
            "_id": ObjectId("874f95ad9ad656bffa5da9be"),
            "tweet_id": ObjectId("c097ab367dd3af86649b7323"),
            "retweet_id": ObjectId("847f1d1ceda9598f91a95b4b")
        },
        {
            "_id": ObjectId("80a823e1a700192911c43ab8"),
            "tweet_id": ObjectId("ae52f4016c8cc3af31cd9c84"),
            "retweet_id": ObjectId("fc607b2259b83468f425c585")
        },
        {
            "_id": ObjectId("b8e8ed895e0c2a7d4d69d8ff"),
            "tweet_id": ObjectId("c03ba6a65a5696fa2865d059"),
            "retweet_id": ObjectId("1afed15ab32282bbcebce243")
        },
        {
            "_id": ObjectId("01407af7e0ed0d6d7cf3edb3"),
            "tweet_id": ObjectId("c8f34f4fc2451d1209499b55"),
            "retweet_id": ObjectId("480cd211f4aa2afed4bd21da")
        },
        {
            "_id": ObjectId("a1379f3f2e03d476b265e7a5"),
            "tweet_id": ObjectId("2dbbc46c70e1d2490375f06c"),
            "retweet_id": ObjectId("915f6aca33be77328cbe2004")
        },
        {
            "_id": ObjectId("855cdd90d8790e7a7281538c"),
            "tweet_id": ObjectId("4e004fc3c80dceb72de47f10"),
            "retweet_id": ObjectId("1a71fd9d3a819fc88fda5643")
        },
        {
            "_id": ObjectId("9afdac81dc7dce98c4aa3198"),
            "tweet_id": ObjectId("55fda78385d4348fa6c313a4"),
            "retweet_id": ObjectId("0a0853fb92af1ea10390fdde")
        },
        {
            "_id": ObjectId("94f4d67532da22896fba35cf"),
            "tweet_id": ObjectId("3946900def359d98cb0ac0cc"),
            "retweet_id": ObjectId("28c3c13d41b3eaabb7f0221f")
        },
        {
            "_id": ObjectId("8369e1b07c49e008bbaec820"),
            "tweet_id": ObjectId("d7a17530916bc9285a0cf813"),
            "retweet_id": ObjectId("338f276a6092defebd585a84")
        },
        {
            "_id": ObjectId("fca21deec1c41d824e2b45ab"),
            "tweet_id": ObjectId("07d1e0ef2b9439f5ff21f2f2"),
            "retweet_id": ObjectId("475db2d32d8cf1a3f9879b4d")
        },
        {
            "_id": ObjectId("d7104488495f94e44fa47670"),
            "tweet_id": ObjectId("a29a1a940c5c6621b2fd40e8"),
            "retweet_id": ObjectId("7dfbd709b69d10d40c17a8ac")
        },
        {
            "_id": ObjectId("1a879d64fcff8f1069514962"),
            "tweet_id": ObjectId("c473e3b0024b5b5b0c4f15fb"),
            "retweet_id": ObjectId("0148d07468f5337b88397b4b")
        },
        {
            "_id": ObjectId("ca9fd0919bedfadd9fd90686"),
            "tweet_id": ObjectId("06d261d8ab5d1dd29bad9c75"),
            "retweet_id": ObjectId("87b7a2c1211e6b168cdae5a2")
        }
    ]
)

# Print the number of documents inserted
print(f"{len(result.inserted_ids)} documents were inserted into the 'RETWEET' collection.")