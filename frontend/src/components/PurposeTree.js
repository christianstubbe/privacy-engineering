import React, {useContext, useEffect, useState} from 'react';
import { TreeContext } from '../TreeContext';
import { Chip } from '@mui/material';
import ArrowDropDownIcon from '@mui/icons-material/ArrowDropDown';
import ArrowRightIcon from '@mui/icons-material/ArrowRight';
import TreeView from '@mui/lab/TreeView';
import TreeItem from '@mui/lab/TreeItem';


const PurposeTree = () => {
  const { treeData, isLoading } = useContext(TreeContext);
  const [expanded, setExpanded] = useState([]);

  useEffect(() => {
    const getAllNodeIds = (nodes) => {
      return nodes.reduce((acc, node) => {
        return [...acc, node.purpose_id, ...getAllNodeIds(node.children || [])];
      }, []);
    };
    setExpanded(getAllNodeIds(treeData));
  }, [treeData]);

  const renderLabel = (nodeId, label, transformations) => (
    <div>
      <div>{label}</div>
      <div>Transformations:
        {transformations.map(transformation => (
          <Chip
            key={transformation}
            label={transformation}
            color={'primary'}
          />
        ))}
        </div>
    </div>
  );

  const renderTree = (nodes) => (
    nodes.map((node) => (
      <TreeItem
          key={node.purpose_id}
          nodeId={node.purpose_id.toString()}
          label={renderLabel(node.purpose_id, node.name, node.transformations)}>
        {Array.isArray(node.children) ? renderTree(node.children) : null}
      </TreeItem>
    ))
  );

  if (isLoading) {
    return <div>Loading...</div>;
  }

  return (
    <TreeView
      defaultCollapseIcon={<ArrowDropDownIcon />}
      defaultExpandIcon={<ArrowRightIcon />}
      defaultExpanded={expanded}
      multiSelect
    >
      {renderTree(treeData)}
    </TreeView>
  );
}

export default PurposeTree;
