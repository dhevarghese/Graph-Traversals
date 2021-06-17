function visualise(){
    console.log(G.numberOfNodes());
    /**for (i = 1; i <= G.numberOfNodes(); i++) {
      G.node.get(i).color = '#0064C7';
    }*/
    jsnx.draw(G, {
      element: '#demo-canvas',
      withLabels: true,
      nodeStyle: {
        fill: function(d) { 
            return d.data.color;
        }
      }, 
      labelStyle: {fill: 'white'},
    });
  }

  var count = 0;
  var torder = [];

  function setCount() {
    count = 0
  }

  function next() {
    waitInLoopNext(count,torder);
  }

  function prev() {
    waitInLoopPrev(count,torder);
  }
  
  function waitInLoopPrev(node, ord) {
    setTimeout(function() {
      count = count - 1;
      G.node.get(torder[count]).color = '#0064C7';
      jsnx.draw(G, {
        element: '#demo-canvas',
        withLabels: true,
        nodeStyle: {
          fill: function (d) {
            return d.data.color;
          }
        },
        labelStyle: { fill: 'white' },
      });
    }, 750)  
  }

  function waitInLoopNext(node, ord) {
    setTimeout(function() {
      G.node.get(ord[node]).color = 'green';
      count = count + 1                                                                                                     
      jsnx.draw(G, {
        element: '#demo-canvas',
        withLabels: true,
        nodeStyle: {
          fill: function(d) { 
              return d.data.color;
          }
        }, 
        labelStyle: {fill: 'white'},
      });
      /*
      node++;
      if (node<ord.length) {
        console.log("in if cond");
        waitInLoop(node, ord);
      }*/
    }, 750)
    
  } 

  function visualiseTraversal(ord){
    var i = 0;
    setCount();
    torder = ord;
    var itr;
    for (let curNode of G){
        console.log(curNode);
        G.node.get(curNode).color = '#0064C7';  
    }
    waitInLoopNext(0, ord);
  }

  function print1(m)
  {
    document.getElementById("ds").innerHTML ="";
    /*var dump = JSON.stringify(m, null, 4); 
    $('#dump').html(dump)*/
    console.log(document.getElementById("ds"))
    console.log(m)
    var s=""
    for(var i=1;i<m.length;i++){
      for(var j=1;j<m.length;j++){
        //document.getElementById("ds").append(`<span>${m[i][j]}</span>`)
        if(m[i][j]!=undefined)
          s+=`<span>${m[i][j]} </span>`
          
          
      }
      //document.getElementById("ds").append("<br>")
      s+='<br>'
    }
    console.log(s)
    document.getElementById("ds").innerHTML =s;
    document.getElementById("ds").style.padding = "50px 10px 20px 30px";
    /*var tbl = prettyPrint( m);
    document.getElementById("ds").appendChild(tbl);*/
  }

  function print2(m){
    document.getElementById("ds").innerHTML = "";
    var s=""
    for(var i=0;i<m.length;i++){
      s+=`<span>${m[i]} </span>`
      s+='<br>'
    }
    document.getElementById("ds").innerHTML =s;
    document.getElementById("ds").style.padding = "50px 10px 20px 30px";
  }

  function print2TEXT(m){
    document.getElementById("ds").innerHTML = "";
    var s="ADJACENCY LIST \n\n";
    for(var i=0;i<m.length;i++){
      s+=`${m[i]}`
      s+='\n'
    }
    return s;
  }

  function print1TEXT(m)
  {
    document.getElementById("ds").innerHTML ="";
    /*var dump = JSON.stringify(m, null, 4); 
    $('#dump').html(dump)*/
    console.log(document.getElementById("ds"))
    console.log(m)
    var s="ADJACENCY MATRIX \n\n";
    for(var i=1;i<m.length;i++){
      for(var j=1;j<m.length;j++){
        //document.getElementById("ds").append(`<span>${m[i][j]}</span>`)
        if(m[i][j]!=undefined)
          s+=`${m[i][j]} `
          
          
      }
      //document.getElementById("ds").append("<br>")
      s+='\n'
    }
    return s;
    /*var tbl = prettyPrint( m);
    document.getElementById("ds").appendChild(tbl);*/
  }