function generate_row(element)
{
    //console.log($(element).closest('tr'))
    var row = []
    td_elements = $($(element).closest('tr')).children()
    td_elements.each(function(i)
    {
        if (i != td_elements.length-1)
        {
            row.push($(this).text());
        }
        
        
    });
    return row.join(",");
}
function generate_header()
{
    var row = []
    $("#my-table thead tr th").each(function(i){
        //console.log($(this).html());
            if ($(this).html() != "Select")
            {
                row.push($(this).html());
            }
    });
    return row.join(",");
}


function validate_selection()
{
    
  if ($('input[name="checkbox"]:checked').length > 0 )    
  {
      return true;
  }
  return false;
}

function prepare_data()
{
            var checked_boxes =  $('input[name="checkbox"]:checked');
            var csvdata = []
            csvdata.push(generate_header())
            $(checked_boxes).each(function(index){

                csvdata.push(generate_row($(this)));
            });
        if(csvdata.length > 0 )
        {
            return csvdata.join("\n");
        }
        return undefined;
}
function create_file(csvdata)
{
    try{
        var csvfile = new Blob([csvdata],{type:"text/csv"});
        return csvfile;
    }
    catch(e)
    {
        console.error(e);
        return undefined;
    }
    
}
function prepare_request(csvfile,token,url)
{
    var user_data = user_data_read();
    var formData = new FormData()
    formData.append('csrfmiddlewaretoken', token);
    formData.append('Full_name',user_data[0]);
    formData.append('email_id',user_data[1]);
    formData.append('mobile_number',user_data[2]);
    var filename = user_data[0]+"_"+user_data[2]+".csv";
    formData.append("file" , csvfile,filename);
    $.ajax({
        url:url,
        type:"post",
        data:formData,
        processData:false,
        contentType:false,
        success:function(response){
            ack = parseInt(response);
            $("#exampleModalCenter").modal("hide");
            $("body").scrollTop();
            if (ack  > 0 )
            {
                
                if (ack == 1) {
                    if (toggle_msg_class(1)) {
                        msg_show("Your Free Sample Request Recieved We Back To You very soon");
                    }
                }
                else if (ack == 2) {
                    if (toggle_msg_class(2)) {
                        msg_show("Server Error While Processing Your Request!!!! Please Try Again or contact Customer Care");
                    }
                }
                else if (ack = undefined) {
                    if (toggle_msg_class(2)) {
                        msg_show("Unknown Error Occur At server Please Try again Later");
                    }
                }
                else {
                    if (toggle_msg_class(2)) {
                        msg_show("Unknown Error Occur  Please Contact Customer Support");
                    }
                }
            }
            else
            {
                return undefined;
            }
            $("#ack_msg").show();        
        }
    });
}

function toggle_msg_class(type)
{
    if(type == 1) // for success msg
    {
        if($("#ack_msg").hasClass("alert-success"))
        {
            return true;
        }
        else if ($("#ack_msg").hasClass("alert-danger"))
        {
            $("#ack_msg").removeClass("alert-danger")
            $("#ack_msg").addClass("alert-success")
            return true;
        }
        else
        {
            $("#ack_msg").addClass("alert-success")
            return true;
        }
    }
    else if (type == 2)
    {
        if($("#ack_msg").hasClass("alert-danger"))
        {
            return true;
        }
        else if ($("#ack_msg").hasClass("alert-success"))
        {
            $("#ack_msg").removeClass("alert-success");
            $("#ack_msg").addClass("alert-danger");
            return true;
        }
        else
        {
            $("#ack_msg").addClass("alert-danger");
            return true;
        }
    }
return false;
}

function msg_show(msg)
{
    $("#ack_msg").show();
    $("#ack_msg").html(msg);
}

function validate_user_details()
{
    var full_name = $("#full_name").val();
    var email_id = $("#exampleInputEmail1").val();
    var mobile_number = $("#exampleInputmobile").val();
    var error_filed = []
    if(full_name.length < 5)
    {
        error_filed.push("> Not Valid Name Enter Your Full Name");
    }
    if (!/^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/.test(email_id))
    {
        error_filed.push("> Invalid Email Id");
    }
    if(mobile_number.length > 10 || mobile_number.length <= 0 || mobile_number.length != 10)
    {
        error_filed.push("> Invalid Mobile Number");
    }
    if(error_filed.length == 0)
    {
        return [];
    }
    else
    {
        return error_filed;
    }
    
}
function user_data_read()
{
    var full_name = $("#full_name").val();
    var email_id = $("#exampleInputEmail1").val();
    var mobile_number = $("#exampleInputmobile").val();
    return [full_name,email_id,mobile_number]
}