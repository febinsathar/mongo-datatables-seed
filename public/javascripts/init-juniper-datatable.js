$(document).ready(function() {
  $('#juniper-table tfoot th').each(function() {
    var title = $('#juniper-table tfoot th').eq($(this).index()).text();
    $(this).html('<input type="text" placeholder="Search ' + title + '"/>');
  });

  var table = $('#juniper-table').DataTable({
    serverSide: true,
    processing: true,
    autoWidth: true,
    ajax: 'data.json',
    columns: [
      	{ data: "script_name",name:"script_name" },
			{
				data: "path",name:"path",
				render: function (data, type, full, meta) {
					return '<a href="' + data + '">' + 'cvs link' + '</a>'
				},
			},
			{ data: "RLI",name:"RLI",searchable:true },
			{ data: "TPI" ,name:"TPI"},
			{ data: "PR",name:"PR" },
			{ data: "protocol" ,name:"protocol"},
			{ data: "subareas",name:"subareas" }
    ]
  });

  $('#juniper-table')
    .removeClass('display')
    .addClass('table table-stripped table-bordered');

  table.columns().every(function() {
    var that = this;

    $('input', this.footer()).on('keyup change', function() {
 if ( that.search() !== this.value ) {
      that
        .search(this.value)
        .draw();
    }
    });
    
  });
});