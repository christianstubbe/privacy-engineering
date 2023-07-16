import React, { useContext } from 'react';
import { TreeContext } from '../Context';
import { Chip } from '@mui/material';
import ArrowDropDownIcon from '@mui/icons-material/ArrowDropDown';
import ArrowRightIcon from '@mui/icons-material/ArrowRight';
import TreeView from '@mui/lab/TreeView';
import TreeItem from '@mui/lab/TreeItem';


const PurposeTree = () => {
  const { treeData, isLoading } = useContext(TreeContext);
  const [selectedTransformations, setSelectedTransformations] = React.useState({});

  const handleChipClick = (nodeId, transformation) => {
    setSelectedTransformations(prev => ({
      ...prev,
      [nodeId]: {
        ...prev[nodeId],
        [transformation]: !prev[nodeId]?.[transformation],
      },
    }));
  };

  const renderLabel = (nodeId, label, transformations) => (
    <div>
      <div>{label}</div>
      <div>Transformations: </div>
      <div>
        {transformations.map(transformation => (
          <Chip
            key={transformation}
            label={transformation}
            clickable
            color={selectedTransformations[nodeId]?.[transformation] ? 'primary' : 'default'}
            onClick={() => handleChipClick(nodeId, transformation)}
          />
        ))}
      </div>
    </div>
  );

  const renderTree = (nodes) => (
    nodes.map((node) => (
      <TreeItem nodeId={node.purpose_id.toString()} label={renderLabel(node.purpose_id, node.name, node.transformations)}>
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
      multiSelect
    >
      {renderTree(treeData)}
    </TreeView>
  );
}

export default PurposeTree;
