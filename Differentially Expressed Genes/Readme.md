
# Differential Gene Expression

## Network Construction of differentially expressed gene :

A differential network analysis compares individual networks from different populations, or groups, to identify group-specific connections. Differences in the topology of two networks may indicate differences in the underlying cellular activity. For example, the existence of differentially connected (DC) gene modules might indicate that various pathways have been rewired.

![Image depicting final network construction using differential expression](https://github.com/Rahul-Ganesan/Bioinformatics-and-Biological-Systems/blob/db858d2df41c002bf2fbf91dcb3bb5a81a35a370/Differentially%20Expressed%20Genes/One.png)

i)Networks inferred from gene expression data are called gene co-expression networks (GCN).

ii)These are undirected graphs with nodes representing genes and edges representing gene-gene associations.

iii)The topology of the inferred network is used to make predictions about the genes. 

iv)For example, a hub gene in the network may be a transcription factor that regulates its connected genes. Or, a connected component in the network might be a set of genes involved in a particular pathway or protein complex.

## Centrality Measure

i) The structural analysis of biological networks includes the ranking of the vertices based on the connection structure of a network.

ii) To support this study we discuss centrality measures which indicate the importance of vertices, demonstrate their applicability on a gene regulatory network. 

iii) We show that common centrality measures result in different valuations of the vertices and that novel measures tailored to specific biological investigations are useful for the analysis of biological networks, in particular gene regulatory networks.

### Local Based Method and Global Based Method

i) To calculate the score of a node within a network, a local rank method only considers the relationship between the node and its direct neighbours 
global method examines the relationship between the node and the entire network.

We have 11 node ranking methods to evaluate the importance in biological networking.

Local Based Methods

1. Degree method (Deg)
2. Maximum Neighborhood Component (MNC)
3. Density of Maximum Neighborhood Component (DMNC)
4. Maximal Clique Centrality (MCC)

Global Based Methods

1. Closeness (Clo)
2. EcCentricity (EC)
3. Radiality (Rad)
4. BottleNeck (BN)
5. Stress (Str)
6. Betweenness (BC)
7. Edge Percolated Component (EPC)

## String Enrichment Analysis

String Enrichment Analysis is a method to identify classes of genes and proteins that are over – represented in a large set of gene or protein , and may have an association with disease phenotypes. 

The method uses statistical approaches to identify significantly enriched or depleted groups of genes. 

Transcriptomics technologies and proteomics results often identify thousands of genes which are used for the analysis.

## Results

String Network Constructed from differentially expressed genes

![](https://github.com/Rahul-Ganesan/Bioinformatics-and-Biological-Systems/blob/f8c664f1cce509769173b7089c361c5d9a866f82/Differentially%20Expressed%20Genes/STRING%20network.png)

## Resources and Software Used

[Cytoscape](https://cytoscape.org/)

[CytoHubba](https://bmcsystbiol.biomedcentral.com/articles/10.1186/1752-0509-8-S4-S11)

[Gene Ontology Term Enrichment Analysis](https://pubmed.ncbi.nlm.nih.gov/27780226/)
