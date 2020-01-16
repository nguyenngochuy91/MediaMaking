#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 18:14:15 2020

@author:  huynguyen,nhivan
@project: media making
"""
import pydot
import json
from IPython.display import Image, display
import os,platform

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
                          "Children:":{} } } 
        # print (self.name)
        children = self.getChildren()
        for child in children:
            childDic = child.generateDictionary()
            # print (childDic)
            dic[self.name]["Children:"].update(childDic)
        return dic
    # generate a digraph to visualization
    def generateGraph(self):
        # generate a digraph for Dot
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
            newNode = pydot.Node(info)
            newNode.obj_dict['name'] = info
            nodeToName.append((newNode,name))
            parent = node.getParent()
            if parent:
                newE      = pydot.Edge(d[parent],d[node],color="blue")
                graph.add_edge(newE)
            else:
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