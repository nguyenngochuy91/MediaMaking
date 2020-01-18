#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 18:14:15 2020

@author:  huynguyen,nhivan
@project: media making
"""
import pydot
import json


class Bottle:
    def __init__(self,name,ph,date,notes,children,parent = None):
        self.name = name
        self.date = date
        self.notes = notes
        self.children = children
        self.parent = parent
        self.ph = ph
        
    ## method to get the attributes
    def getParent(self):
        return self.parent
    def getChildren(self):
        return self.children
    def getName(self):
        return self.name
    def getDate(self):
        return self.date 
    def getNotes(self):
        return self.notes
    def getPh(self):
        return self.ph
    # modify 
    def updateNote(self,newNote):
        self.notes += newNote 
    def updateDate(self,date):
        self.date = date 
    def updateName(self,name):
        self.name = name
    def updateChildren(self,children):
        for child in children:
            self.children.append(child)
            child.parent = self
    # generate a dictionary for the tree rooted at self
    def generateDictionary(self):
        dic = {self.name:{"Date:":self.date,
                          "Ph:":self.ph,
                          "Notes:":self.notes,
                          "Children:":{} , "Parent:": self.parent.name if self.parent else None} 
                          } 
        # print (self.name)
        children = self.getChildren()
        for child in children:
            childDic = child.generateDictionary()
            # print (childDic)
            dic[self.name]["Children:"].update(childDic)
        return dic
    # generate a digraph to visualization
    def generateGraph(self,updateNodes =set(),childNodes = set()):
        # generate a digraph for Dot
        print ("updateNodes:",updateNodes)
        print ("ChildNodes:",childNodes)
        graph = pydot.Dot(graph_type='digraph')
        queue = [self]
        d = {}
        nodeToName = []
        while queue:
            node = queue.pop()
            name = node.getName()
            date = node.getDate()
            ph   = node.getPh()
            notes = node.getNotes()
            info = "name: {}\ndate: {}\npH: {}\nnotes: {}".format(name,date,ph,notes)
            d[node] = info
            # generate newNode
            if updateNodes:
                if name in updateNodes:
                    newNode =pydot.Node(name,style="filled", fillcolor="pink") 
                else:
                    newNode =pydot.Node(name)
            else:
                newNode =pydot.Node(name)
            if childNodes:
                if name in childNodes:
                    print (84,name)
                    newNode =pydot.Node(name,style="filled", fillcolor="green")
                else:
                    newNode =pydot.Node(name)
            else:
                newNode =pydot.Node(name)
            newNode.obj_dict['name'] = info
            nodeToName.append((node,name))
            parent = node.getParent()
            if parent:
                if childNodes:
                    if name in childNodes:
                        newE      = pydot.Edge(d[parent],d[node],color="blue")
                    else:
                        newE      = pydot.Edge(d[parent],d[node],color="black")
                else:
                    newE      = pydot.Edge(d[parent],d[node],color="black")
                graph.add_edge(newE)
            graph.add_node(newNode)        
            # attribute = G[parent][children]
            # v         = float(attribute['volume'])
            # add       = float(attribute['add'])
            # if attribute["type"] =="update":
            #     newE      = pydot.Edge(d[parent],d[children],color="blue")
            # else:
            #     newE      = pydot.Edge(d[parent],d[children], label ="{}ml+{}ml".format(v-add,add),fontsize="10.0", color="black")
            # graph.add_edge(newE)
            children = node.getChildren()
            for child in children:
                queue.append(child)
        return graph,nodeToName
    # return a dictionary that maps each node from the root to its name, do so in bfs maner
    def generateNames(self):
        graph,nodeToName = self.generateGraph()
        nameToNode = {}
        for node,nodeName in nodeToName:
            nameToNode[nodeName] = node
        return nodeToName,nameToNode
        
        
    ## write to a jason file using dic
    def writeJSON(self,outputFile):
        dic = self.generateDictionary()
#        print (dic)
        try:
            json.dump(dic, outputFile,indent=4)
        except:
            string = json.dumps(dic,indent=4)
            with open(outputFile,"w") as handle:
                handle.write(string)
    ## write pydot file to a png
    def writePNG(self,outputFile):
        graph,nodeToName = self.generateGraph()
        graph.write_png(outputFile)
        
    # loading a dic file, and return a bottle object
    def load(self,dictionary):
        def dfs(currentNode,dictionary):
            if dictionary:
                children = []
                for child in dictionary:
                    name = child
                    notes = dictionary[child]["Notes:"]
                    parent = dictionary[child]["Parent:"]
                    ph = dictionary[child]["Ph:"]
                    date = dictionary[child]["Date:"]
                    bottle = Bottle(name,ph,date,notes,[],parent)
                    dfs(bottle,dictionary[name]["Children:"])
                    children.append(bottle)
                currentNode.updateChildren(children)
        name,dic = dictionary.popitem()
        bottle = Bottle(name,dic["Ph:"],dic["Date:"],dic["Notes:"],[],None)
        dfs(bottle,dic["Children:"])
        return bottle
    
    # return a deep copy of itself
    def deepCopy(self):
        def dfs(currentNode):
            newNode = Bottle(currentNode.name,currentNode.ph,currentNode.date,currentNode.notes,[],currentNode.parent)
            children = []            
            for child in currentNode.children:
                newChild = dfs(child)
                children.append(newChild)
            newNode.updateChildren(children)
            return newNode
        return dfs(self)
    # given self, and a node name, return the dictionary of nodename to node
    def find(self,nodeNames):
        dic = {}
        def dfs(node):
            if node.name in nodeNames:
                dic[node.name] = node
            for child in node.children:
                dfs(child)
        dfs(self)
        return dic
    # given a dictionary update all the node with children 
    def updateAllNodes(self,parentNameToNodes):
        dic = self.find([name for name in parentNameToNodes])
        # print (parentNameToNodes)
        # print (dic)
        # for each of the name, we get the list of info, create a bottle object, then update our node
        for name in parentNameToNodes:
            myList = parentNameToNodes[name]
            node = dic[name]
            children = []
            for newName,ph,date,notes in myList:
                bottle = Bottle(newName, ph,date,notes, [],None)
                children.append(bottle)
            node.updateChildren(children)
    
A = Bottle("A",1,"",7,[],None)
AA = Bottle("AA",1,"",7,[],None)
AB = Bottle("AB",1,"",7,[],None)
AC = Bottle("AC",1,"",7,[],None)
AD = Bottle("AD",1,"",7,[],None)
A.updateChildren([AA,AB,AC,AD])

AAA = Bottle("AAA",1,"",7,[],None)
AAB = Bottle("AAB",1,"",7,[],None)
AA.updateChildren([AAA,AAB])
A.writeJSON("data")
#dictionary =json.load(open("data","r"))
#B = Bottle("",0,"",0,[],None)
#C = B.load(dictionary)
B = A.deepCopy()