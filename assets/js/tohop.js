var nvong = {
    "7580201C" : {
        "name" : "Kỹ thuật xây dựng (Chất lượng cao)",
        "tohop": ["A00","A01"],
        "id": 1
    },

    "7580201H" : {
        "name" : "Kỹ thuật xây dựng - Học tại khu Hòa An",
        "tohop" : ["A00","A01"],
        "id": 2
    },

    "7380101" : {
        "name" : "Luật",
        "tohop" : ["B00"],
        "id": 3
    },

    "7380101H" : {
        "name" : "Luật (Luật hành chính) - Học tại khu Hòa An",
        "tohop" : ["B00","D01"],
        "id": 4
    },

    "7340115" : {
        "name" : "Marketing",
        "tohop" : ["B00","D01"],
        "id": 5
    },
    "7480102" : {
        "name" : "Mạng máy tính và truyền thông dữ liệu",
        "tohop" : ["A00","A01"],
        "id": 6
    }
};
var tohop = {
    "A00" : {
        "name" : "To hop A00",
        "subject": ["Toán","Lý","Hóa"],
        "string": "Toán, Lý, Hóa",
        "slug" : ["toan","ly","hoa"],
        "id": 1
    },

    "A01" : {
        "name" : "To hop A01",
        "subject" : ["Toán","Lý","Anh văn"],
        "string" : "Toán, Lý, Anh văn",
        "slug" : ["toan","ly","anhvan"],
        "id": 2
    },

    "B00" : {
        "name" : "To hop B00",
        "subject" : ["Toán","Hóa","Sinh"],
        "string" : "Toán, Lý, Sinh",
        "slug" : ["toan","ly","sinh"],
        "id": 3
    },

    "D01" : {
        "name" : "To hop D01",
        "subject" : ["Toán","Văn","Anh văn"],
        "string" : "Toán, Văn, Anh văn",
        "slug" : ["toan","van","anhvan"],
        "id": 4
    }

};

function change_nvong(){
    var id = document.getElementById("nv1").value;
    var arr = nvong[id].tohop;
    var th = document.getElementById("th1");
    while (th.options.length > 1) {
        th.remove(0);
    }
    document.getElementById("score_input").innerHTML = "";
    arr.forEach(function (entry,index) {
        // console.log(index);
        // var name_th = tohop[entry].string;
        // console.log(name_th);
        var option = document.createElement("option");
        option.text = tohop[entry].string;
        option.value = entry;
        th.add(option,th[index]);
        var subs = tohop[entry].subject;
    });
}

function change_score_input(){
    var th = document.getElementById("th1");
    console.log(th.value);

    var arr = tohop[th.value].subject;
    // console.log(arr);
    var slug = tohop[th.value].slug;
    var innerHTML = "";


    for(var i = 0; i < arr.length; i++){
        console.log(arr[i]);
        var div = document.getElementById("score_input");
        innerHTML += '                    <div class="score-row">\n' +
            '                        <div class="col-md-1">\n' +
            '                            <h5>'+arr[i]+'</h5>\n' +
            '                        </div>\n' +
            '                        <div class="col-md-2">\n' +
            '                            <input id="'+slug[i]+'10_hk1" name="'+slug[i]+'10_hk1" type="number" max="10" min="0">\n' +
            '                        </div>\n' +
            '                        <div class="col-md-2">\n' +
            '                            <input id="'+slug[i]+'10_hk2" name="'+slug[i]+'10_hk2" type="number" max="10" min="0">\n' +
            '                        </div>\n' +
            '                        <div class="col-md-2">\n' +
            '                            <input id="'+slug[i]+'11_hk1" name="'+slug[i]+'11_hk1" type="number" max="10" min="0">\n' +
            '                        </div>\n' +
            '                        <div class="col-md-2">\n' +
            '                            <input id="'+slug[i]+'11_hk2" name="'+slug[i]+'11_hk2" type="number" max="10" min="0">\n' +
            '                        </div>\n' +
            '                        <div class="col-md-2">\n' +
            '                            <input id="'+slug[i]+'12_hk1" name="'+slug[i]+'12_hk1" type="number" max="10" min="0">\n' +
            '                        </div>\n' +
            '                        <div class="col-md-1">\n' +
            '                            <input id="'+slug[i]+'TB" name="'+slug[i]+'TB" type="number" max="10" min="0">\n' +
            '                        </div>\n' +
            '                    </div>\n';

        div.innerHTML = innerHTML;
    }
}